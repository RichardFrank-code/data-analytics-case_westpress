# 📊 Data Analytics Case – Westpress  
Automatisierter Kundenreport & Performance-Dashboard

Dieses Repository enthält die vollständige Umsetzung des Westpress Analytics-Cases:

✔ Anforderungen mit Stakeholder aufgenommen  
✔ Daten bereinigt (Python ETL)  
✔ Star-Schema erstellt  
✔ Power BI Backend gebaut  
✔ Management-Dashboard + Kundenreport erstellt  
✔ Präsentation finalisiert  

---

## 🚀 Setup (lokale Entwicklung)

```bash
git clone <repo-url>
cd <repo-name>
python -m venv .venv
.\.venv\Scripts\activate   # Windows
pip install -r requirements.txt
🗂 Projektstruktur
powershell
Code kopieren
.
├── docs/
│   ├── requirements.md        # Stakeholder-Anforderungen (WHAT)
│   ├── concept.md             # Architektur & ETL-Konzept (HOW)
│   └── timeplan.md            # Vorgehen / Planung
│
├── notebooks/
│   └── 01_EDA_umsatz_tracking.ipynb   # Exploration / Prototyping
│
├── src/
│   └── etl_clean_sales_tracking.py    # finaler ETL Pipeline
│
├── data/                               # lokale Daten (NICHT im Repo)
│   ├── Umsatzdaten.xlsx
│   └── Trackingdaten.xlsx
│
├── .gitignore
├── requirements.txt
├── Westpress Data Case – Analyse & Reporting.pptx
└── README.md
## 🔒 Data Governance
Die Originaldaten werden nicht versioniert.
.gitignore schließt folgende Dateien vollständig aus:

/data/*

*.xlsx

*.csv

*.parquet

Versioniert werden ausschließlich:

ETL-/Analyseskripte

Dokumentation (/docs)

Jupyter Notebook ohne Daten

## Präsentation

🏗 Lösungskonzept (Kurzfassung)
1. ERP-Export (Excel)
→ monatlich durch das Unternehmen

2. Python ETL

Datumsfehler korrigiert

Strings bereinigt

Keyword-basierte Job-Family-Klassifikation

Star-Schema generiert (Facts / Date / Customer / JobFamily)

3. Power BI Backend

Datenmodell aufgebaut

Measures definiert

Dashboards erstellt

4. Output

Interaktive Power BI Dashboards

Exportierbare Excel-Reports

Präsentation der Insights

## 📊 Final Deliverables
🟦 Management Dashboard

🟩 Stakeholder-Kundenreport

📝 Präsentation „Analyse & Reporting“

🧪 Python ETL (vollständig reproduzierbar)

✅ Projektstatus
✔ Anforderungen abgeschlossen
✔ ETL finalisiert
✔ Datenmodell final
✔ Dashboards final
✔ Präsentation final

Das Projekt ist vollständig abgeschlossen und reproduzierbar.