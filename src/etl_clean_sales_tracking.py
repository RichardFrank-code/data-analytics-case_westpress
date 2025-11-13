import pandas as pd
import numpy as np
from pathlib import Path
import json
# ======================================================
# TODO / Weitere Verbesserungen (Teilweise bereits in der EDA umgesetzt)
# ======================================================

# 1. JSON-Keywordliste für Job-Family erweitern
#    - Mehr Synonyme ergänzen
#    - Optional: Auslagerung in externe JSON/YAML-Konfig

# 2. ETL-Struktur langfristig modularisieren
#    - Extraktion / Transformation / Laden trennen
#    - Mapping- und Hilfsfunktionen in eigene Module auslagern

# 3. Datenqualität weiter verbessern
#    - Dublettenprüfung, Outlier-Checks etc. (bereits in der EDA erfolgt)
#    - Weitere Textnormalisierung für HEADLINE / PRODUCT_NAME
#    - Validierung der BC_NUMBER-Struktur

# 4. Dimensionstabellen ausbauen
#    - Einheitliche Surrogate Keys für alle DIMs
#    - Optional: Vorbereitung für Slowly Changing Dimensions (SCD)

# 5. Konfiguration vereinheitlichen
#    - Filepaths und Parameter in config.json auslagern
#    - Erweiterung um Logging für ETL-Läufe

# ======================================================
# PATH SETUP
# ======================================================

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
OUTPUT_DIR = DATA_DIR / "cleaned"
OUTPUT_DIR.mkdir(exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "cleaned_data.xlsx"

umsatz_file = DATA_DIR / "Umsatzdaten.xlsx"
tracking_file = DATA_DIR / "Trackingdaten.xlsx"

print("Loading raw files:")
print(" →", umsatz_file)
print(" →", tracking_file)


# ======================================================
# 1. LOAD RAW FILES
# ======================================================

sales = pd.read_excel(umsatz_file)
track = pd.read_excel(tracking_file)


# ======================================================
# 2. RAW DATE COLUMN COPY
# ======================================================

sales["DATE_raw"] = sales["DATE"]
track["DATE_raw"] = track["DATE"]


# ======================================================
# 3. FIX INVALID DATE VALUES
# ======================================================

invalid_date = "29.02.2025"
sales.loc[sales["DATE_raw"] == invalid_date, "DATE_raw"] = "28.02.2025"
track.loc[track["DATE_raw"] == invalid_date, "DATE_raw"] = "28.02.2025"


# ======================================================
# 4. PARSE DATES CLEANLY
# ======================================================

sales["DATE"] = pd.to_datetime(sales["DATE_raw"], dayfirst=True, errors="coerce")
track["DATE"] = pd.to_datetime(track["DATE_raw"], dayfirst=True, errors="coerce")


# ======================================================
# 5. DROP INVALID DATES
# ======================================================

sales_clean = sales.dropna(subset=["DATE"]).copy()
track_clean = track.dropna(subset=["DATE"]).copy()


# ======================================================
# 6. CLEAN TYPES & NORMALIZE STRINGS
# ======================================================

sales_clean["BC_NUMBER"] = sales_clean["BC_NUMBER"].astype(str).str.strip()
track_clean["BC_NUMBER"] = track_clean["BC_NUMBER"].astype(str).str.strip()

if "COMPANY_NAME" in sales_clean.columns:
    sales_clean["COMPANY_NAME"] = sales_clean["COMPANY_NAME"].astype(str).str.strip()

if "VIEWS" in track_clean.columns:
    track_clean["VIEWS"] = pd.to_numeric(track_clean["VIEWS"], errors="coerce").fillna(0)


# ======================================================
# 6.5 JOB FAMILY MAPPING
# ======================================================

job_family_mapping = json.loads("""
{
  "job_family": [
    {"name": "Medizin & Pflege", "keywords": ["arzt","ärzt","medizin","klinikum","klinik","pflege","pfleger","gesundheit","krankenhaus","medizinisches zentrum","arztpraxis"]},
    {"name": "Bildung & Lehre", "keywords": ["schule","lehrer","lehrkraft","dozent","professor","hochschule","fachhochschule","universität","uni ","bildung","akademie","pädagog","weiterbildung","bildungszentrum"]},
    {"name": "Verwaltung & Büro", "keywords": ["verwaltung","verwaltungs","sachbearbeiter","büro","office","assistenz","assistenz der geschäftsführung","backoffice","sekretariat","verwaltungskraft","kommunalverwaltung","behörde","amt "]},
    {"name": "Technik & IT", "keywords": ["it ","informatik","entwickler","developer","software","engineer","ingenieur","systemadministrator","administrator","techniker","technik","support","admin "]},
    {"name": "Recht & Beratung", "keywords": ["anwalt","rechtsanwalt","kanzlei","jurist","recht","steuerberater","steuerberatung","consultant","beratung","berater"]},
    {"name": "Handel & Dienstleistung", "keywords": ["handel","kaufmann","kauffrau","verkauf","vertrieb","sales","kundenbetreuer","kundenservice","service","dienstleistung","account manager","autohandel","einzelhandel"]},
    {"name": "Bau & Handwerk", "keywords": ["bau","baustelle","bauleiter","handwerk","handwerker","installation","installateur","elektriker","meister","gewerbe"]},
    {"name": "Sonstige", "keywords": []}
  ]
}
""")

def map_job_family(headline: str, mapping: dict) -> str:
    if not isinstance(headline, str):
        return "Sonstige"
    text = headline.lower()
    for group in mapping["job_family"]:
        for kw in group["keywords"]:
            if kw in text:
                return group["name"]
    return "Sonstige"


# FACT_Sales → HEADLINE exists
if "HEADLINE" in sales_clean.columns:
    sales_clean["JOB_FAMILY"] = sales_clean["HEADLINE"].apply(
        lambda x: map_job_family(x, job_family_mapping)
    )
else:
    sales_clean["JOB_FAMILY"] = "Unbekannt"

# FACT_Tracking → no headline
track_clean["JOB_FAMILY"] = "Unbekannt"


# ======================================================
# 6.6 BUILD DIM_JOBFAMILY
# ======================================================

unique_families = sorted(
    set(sales_clean["JOB_FAMILY"].unique()).union(
        set(track_clean["JOB_FAMILY"].unique())
    )
)

dim_jobfamily = pd.DataFrame({
    "JOB_FAMILY_ID": range(1, len(unique_families) + 1),
    "JOB_FAMILY": unique_families
})

family_to_id = dict(zip(dim_jobfamily["JOB_FAMILY"], dim_jobfamily["JOB_FAMILY_ID"]))

sales_clean["JOB_FAMILY_ID"] = sales_clean["JOB_FAMILY"].map(family_to_id)
track_clean["JOB_FAMILY_ID"] = track_clean["JOB_FAMILY"].map(family_to_id)


# ======================================================
# 7. BUILD DIM_CUSTOMERS
# ======================================================

dim_customers = (
    sales_clean[["BC_NUMBER", "COMPANY_NAME"]]
    .drop_duplicates(subset=["BC_NUMBER"])
    .reset_index(drop=True)
    .sort_values("COMPANY_NAME")
)


# ======================================================
# 8. BUILD DIM_DATE
# ======================================================

date_min = min(sales_clean["DATE"].min(), track_clean["DATE"].min())
date_max = max(sales_clean["DATE"].max(), track_clean["DATE"].max()) + pd.DateOffset(months=6)

dim_date = pd.DataFrame({
    "DATE": pd.date_range(start=date_min, end=date_max, freq="D")
})

dim_date["Year"] = dim_date["DATE"].dt.year
dim_date["Month"] = dim_date["DATE"].dt.month
dim_date["MonthName"] = dim_date["DATE"].dt.strftime("%B")
dim_date["YearMonth"] = dim_date["DATE"].dt.strftime("%Y-%m")
dim_date["Quarter"] = dim_date["DATE"].dt.quarter
dim_date["Day"] = dim_date["DATE"].dt.day
dim_date["Weekday"] = dim_date["DATE"].dt.weekday + 1
dim_date["WeekdayName"] = dim_date["DATE"].dt.strftime("%A")
dim_date["IsWeekend"] = dim_date["Weekday"].isin([6, 7]).astype(int)
dim_date["ISO_Week"] = dim_date["DATE"].dt.isocalendar().week


# ======================================================
# 9. EXPORT EVERYTHING
# ======================================================

print("Exporting cleaned data to:", OUTPUT_FILE)

with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:
    sales_clean.to_excel(writer, sheet_name="FACT_Sales", index=False)
    track_clean.to_excel(writer, sheet_name="FACT_Tracking", index=False)
    dim_customers.to_excel(writer, sheet_name="DIM_Customers", index=False)
    dim_date.to_excel(writer, sheet_name="DIM_Date", index=False)
    dim_jobfamily.to_excel(writer, sheet_name="DIM_JobFamily", index=False)

print("\n=======================================")
print("SUCCESS: Cleaned Star Schema exported!")
print(f" → {OUTPUT_FILE}")
print("Sheets included:")
print("   • FACT_Sales")
print("   • FACT_Tracking")
print("   • DIM_Customers")
print("   • DIM_Date")
print("   • DIM_JobFamily")
print("=======================================\n")
