# 📦 Data Analytics Case – Automatisierter Kundenreport

Dieses Projekt demonstriert die Entwicklung eines vollständigen Data-Analytics-Prozesses zur Automatisierung eines kundenbezogenen Reporting-Workflows.
Umgesetzt wurden ein Power-BI-Management-Dashboard, ein automatisierter Excel-Kundenreport sowie eine Python-ETL-Pipeline zur Bereinigung und Modellierung der Umsatz- und Trackingdaten.
Die Ergebnisse wurden zusätzlich in einer kompakten Fallstudien-Präsentation dokumentiert.

---

## 🚀 Setup (lokale Entwicklung)

### Repository klonen
```bash
git clone <repo-url>
cd <repo-name>
```

### Virtuelle Umgebung erstellen
```bash
python -m venv .venv
```

### venv aktivieren
```bash
.\.venv\Scripts\activate   # Windows
source .venv/bin/activate # Mac/Linux
```

### Dependencies installieren
```bash
pip install -r requirements.txt
```

---

## 🗂 Projektstruktur

```text
.
├── docs/
│   ├── requirements.md
│   ├── concept.md
│   └── timeplan.md
│
├── notebooks/
│   └── 01_EDA_umsatz_tracking.ipynb
│
├── src/
│   └── etl_clean_sales_tracking.py
│
├── data/                # nicht im Repo!
│   ├── Umsatzdaten.xlsx
│   └── Trackingdaten.xlsx
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## 🧱 Architektur (Kurzfassung)

Die Lösung basiert auf einer durchgängigen Datenpipeline von der Rohdatenbereitstellung bis zum finalen Kundenreport:

**ERP-Export (Excel/CSV) → Power-BI-Backend (Model, DAX, Refresh) → Automatisierter Excel-Output für Stakeholder**

**Power-BI-Modell:**
- Aufbau eines **Star Schemas**
- **Faktentabellen:**
  - *Sales* (Umsatz)
  - *Tracking* (Aktivitäts- & Nutzungsdaten)
- **Dimensionstabellen:**
  - *Date*
  - *Customer*
  - *JobFamily*

**Automatisierung:**
- Regelmäßige Aktualisierung über **Power BI Refresh**
- Berechnung der Kennzahlen via **DAX**
- Export in Excel als standardisierter Kundenreport

---

## 🔒 Data Governance

- Keine sensiblen Rohdaten im Repository
- `.gitignore` blockiert `/data/*` sowie `.xlsx` und `.csv`
- Versioniert werden ausschließlich:
  - Code (Python, DAX, ETL)
  - Dokumentation
  - Modell- und Reportdefinitionen

---

## 📊 Features & Ergebnis

- Management-Dashboard (KPIs, Visuals, Kostenübersichten)
- Automatisierter Excel-Kundenreport über Power BI Backend
- Parametrisierung zur *Inaktivitätstage-Prognose*
- Ranking-, Status- & Ampellogiken für Kundensegmente
- Verknüpfung von Tracking- und Umsatzdaten für ganzheitliche Analysen
- Durchgängiger automatisierter Analytics-Workflow

---

## 📌 Status

- ✔ Anforderungen aufgenommen
- ✔ Datenmodell gebaut
- ✔ Reports erstellt
- ✔ Präsentation finalisiert
