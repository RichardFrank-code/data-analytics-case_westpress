# Data Analytics Case – Automatisierter Kundenreport

Dieses Repository enthält die Umsetzung des Analytics-Case:
- Anforderungen aufnehmen (Stakeholder-Interview)
- Datenmodell entwerfen (Power BI Backend)
- Report erstellen (Excel als Output / Power BI als Automatisierungsengine)

---

## 🚀 Setup (lokale Entwicklung)

### 1. Repository klonen
```bash
git clone <repo-url>
cd <repo-name>
2. Virtuelle Umgebung erstellen
python -m venv .venv
3. Umgebung aktivieren
Windows
.\.venv\Scripts\activate

Mac/Linux
source .venv/bin/activate

4. Dependencies installieren
pip install -r requirements.txt

🗂 Projektstruktur
.
├── docs/
│   ├── requirements.md     # Stakeholder-Anforderungen (WHAT)
│   ├── concept.md          # Architektur & Lösungskonzept (HOW)
│   └── timeplan.md         # Zeitplanung / Vorgehen
│
├── notebooks/
│   └── 01_EDA_umsatz_tracking.ipynb   # Prototyping / Exploration (not productive)
│
├── src/                    # optional für Scripts (M-Code, DAX exports, Power BI helpers)
│
├── data/                   # lokale Daten (nicht im Repo!)
│   ├── Umsatzdaten.xlsx
│   └── Trackingdaten.xlsx
│
├── .gitignore              # stellt sicher, dass Daten NICHT hochgeladen werden
├── requirements.txt
└── README.md

🔒 Data Governance

Rohdaten werden nicht versioniert.
Durch .gitignore werden .xlsx / .csv / /data/ automatisch ausgeschlossen.

Versioniert wird nur:

Code (Power Query Schritte, DAX)

Dokumentation (docs/)

Notebook (ohne Daten)

🏗 Lösungskonzept (Kurzfassung)

→ Detail siehe docs/concept.md

ERP Export (Excel/CSV)
        ↓
Power BI Backend (Model, Refresh, DAX)
        ↓
Excel Output für Stakeholder

Excel bleibt Output.

Power BI automatisiert die Aktualisierung.

✅ Status

✅ Anforderungen geklärt (requirements.md)

✅ Architektur definiert (concept.md)

⏳ Datenmodellierung (Power BI)

⏳ Erstellung finaler Report + Präsentation