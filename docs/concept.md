# Konzept – Automatisierter Kundenreport (Power BI Backend → Excel Output)

## 1. Zielsetzung (aus dem Stakeholder-Gespräch)

Der Account Manager benötigt eine monatlich aktualisierbare Übersicht, um Kunden effizient zu priorisieren:

- Wer hat zuletzt gekauft?
- Wie oft kaufen Kunden?
- Wie viel Umsatz generieren sie?
- Welche Kunden sind inaktiv und sollten nachgefasst werden?

👉 Fokus: schnelle Priorisierung von Kunden → **Zeit sparen, Umsatz sichern.**

Der Stakeholder möchte den Output **in Excel** erhalten (Arbeitsmittel im Alltag).

---

## 2. Architektur

### Ist-Situation (vom Stakeholder bestätigt)

- Daten stammen aus dem **ERP-System**
- Bereitstellung erfolgt per **monatlichem Export (Excel/CSV)**
- Analyst hat **keinen direkten Zugriff** auf ERP / Datenbank / API

### Lösungsarchitektur (Prozess)

```
ERP Export  (Excel/CSV)
        ↓
Power BI Backend
  • Power Query (ETL)
  • Data Model (Measures, Ranking, KPIs)
  • Automatischer Refresh
        ↓
Excel Output für Stakeholder
  • Export oder Power BI Subscription
```

✅ Power BI automatisiert den Prozess  
✅ Excel bleibt das Lieferartefakt

> **„Excel ist der Output, nicht die Datenquelle.“**

---

## 3. Datenmodell / Transformation (Entwurf – Validierung während EDA)

**Ziel:** Wiederholbare Transformation definieren, die monatlich auf den ERP-Export anwendbar ist.

⚠️ Konkrete Spalten-Details (Bezeichnungen, Datentypen) werden im EDA-Notebook überprüft und anschließend finalisiert.

### Power Query (Draft Steps)

1. Import der ERP-Exportdateien (Excel/CSV)
2. Spaltentypen setzen  
   - Datum → `Date`
   - Umsatz → `Decimal`
   - Kunde/Produkt → `Text`
3. Filter: rolling window, **letzte 12 Monate**
4. Textnormalisierung (Trimmen, Groß-/Kleinschreibung optional vereinheitlichen)
5. Aggregation je Kunde (Group By):
   - `TotalRevenue = Sum(Umsatz)`
   - `OrderCount = Count(Zeilen)`
   - `LastPurchase = Max(Datum)`
6. Laden als Tabelle `CustomerSummary` in das Datenmodell

---

## 3.1 Annahmen, Prüfungen & Risiken (werden in EDA bestätigt)

| Thema | Annahme | Risiko | Umgang |
|--------|---------|--------|--------|
| Datentypen | Datum/Umsatz sind sauber konvertierbar | gemischte Formate | Notebook prüft & bereinigt |
| Kundennamen | stabil genug für Aggregation | unterschiedliche Schreibweisen → Dopplung | Lookup / Mapping-Tabelle möglich |
| Rolling Window | letzte 12 Monate ausreichend | ERP-Daten haben Delay | Parameter anpassbar |
| Datenquelle | Export-Dateien verfügbar | Export nicht durchgeführt | Prozess hängt von ERP ab (Out-of-Scope) |

> Ziel: **prozessfähig ohne manuelle Datenaufbereitung.**

---

## 3.2 Rolle der Notebooks (EDA & Prototyping)

Jupyter-Notebooks werden **gezielt** eingesetzt für:

- Sichtung der gelieferten Dateien (`Umsatzdaten.xlsx`, `Trackingdaten.xlsx`)
- Datentypkontrolle, Missing Values, Duplikate
- Prototypische Aggregation (Umsatz / Letzter Kauf / Ranking)

👉 Die Notebook-Logik wird anschließend **in Power Query/DAX übertragen**  
👉 Rohdaten bleiben **lokal** — `.gitignore` verhindert Upload

> Notebooks = Experimentierfläche  
> Power BI = produktiver ETL + Automatisierung

---

## 4. Berechnungen (DAX – Power BI Backend)

**Gesamtumsatz je Kunde**

```DAX
TotalRevenue = SUM(tbl_sales[Umsatz])
```

**Auftragsanzahl**

```DAX
OrderCount = COUNT(tbl_sales[Datum])
```

**Letzter Kaufzeitpunkt**

```DAX
LastPurchase = MAX(tbl_sales[Datum])
```

**Inaktivitätsflag (Standard = 60 Tage, parameterisierbar)**

```DAX
Inactive =
IF(
    DATEDIFF([LastPurchase], TODAY(), DAY) > 60,
    "Ja",
    "Nein"
)
```

**Ranking nach Umsatz**

```DAX
Rank_Umsatz =
RANKX(
    ALL(tbl_customer),
    [TotalRevenue],
    ,
    DESC,
    Dense
)
```

> KPIs spiegeln die Anforderungen des Stakeholders exakt wider.

---

## 5. Output / Lieferung

Stakeholder erhält:

| Format | Inhalt |
|--------|--------|
| ✅ Excel | fertige kundenpriorisierte Liste |
| optional: Power BI Subscription | Datei wird automatisch monatlich generiert |

Wie aktualisiert der Stakeholder den Report?

1) Neue ERP-Exportdatei ablegen  
2) Power BI: Daten aktualisieren (oder Subscription)  
3) Excel aktualisiert sich automatisch

---

## 6. Data Governance & Sicherheit

- Rohdaten **werden nicht in GitHub gespeichert**
- `.gitignore` blockiert `.xlsx`, `.csv`, `/data/`
- Versioniert werden nur:
  - Code (Power Query M-Skripte, DAX)
  - Dokumentation (`requirements.md`, `concept.md`)
  - Notebook ohne Daten

> Fokus auf Datenschutz & saubere Versionskontrolle.

---

## 7. Skalierung / Zukunftsoption (nicht im Scope)

| Verbesserung | Wirkung |
|--------------|---------|
| ERP → direkte Datenbank-/API-Anbindung | Eliminierung manueller Exporte |
| Automatischer Refresh (Power BI Service) | kein manueller Aufwand |
| Self-Service Dashboard | Wiederverwendbarkeit & Mehrwert im Unternehmen |

> Empfehlung: Nach Übergabe mit IT/Data Engineering prüfen.

---

## 8. Ergebnis

- Stakeholder erhält **Excel**, wie gewünscht
- Analyst arbeitet **automatisiert & skalierbar** über Power BI
- Minimaler manueller Aufwand
- Lösung ist erweiterbar für andere Kunden und KPIs

> **„Excel als Lieferartefakt – Power BI als Automatisierungsmaschine.“**
