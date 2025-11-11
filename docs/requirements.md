# Requirements – Stakeholder-Chat

## Ziel des Gesprächs
Die Anforderungen für einen **monatlich aktualisierbaren Kunden-Performance-Report** erfassen, der dem Account Manager ermöglicht, Kunden nach Relevanz zu priorisieren und Inaktivität zu erkennen.

## Kontext (aus Aufgabenstellung)
- Es handelt sich um einen Probe-Case.
- Stakeholder erwartet einen **automatisierten / regelmäßig nutzbaren Report**.
- Datenquellen: `Umsatzdaten.xlsx` (und optional Trackingdaten).
- Ergebnispräsentation: Freitag um 15:00 Uhr.

---

## Anforderungen aus dem Stakeholder-Gespräch

### 🎯 Ziel
Der Account Manager möchte auf einen Blick sehen:

- Welche Kunden zuletzt gekauft haben
- Welche Kunden aktiv vs. inaktiv sind (seit X Tagen kein Kauf)
- Welche Kunden priorisiert kontaktiert werden sollten

> Fokus: **Betreuung effizient priorisieren**

---

### 📊 KPIs (vom Stakeholder bestätigt)

| KPI | Beschreibung |
|------|-------------|
| letzter Kaufzeitpunkt | wann der Kunde zuletzt gekauft hat |
| Anzahl der Aufträge | wie oft der Kunde im Zeitraum gekauft hat |
| Umsatz | Summe der Käufe im Zeitraum |
| Ranking | Sortierung der Kunden (Top → Low) |
| Inaktivitätsflag | „kein Kauf seit > X Tagen“ |

---

### 🗂 Output-Spalten (vom Stakeholder wörtlich genannt)

| Spalte | Bedeutung |
|--------|-----------|
| **Datum** | Kaufdatum |
| **Kunde** | Kundenname |
| **Produkt** | gekaufte Leistung / Produkt |
| **Umsatz** | Betrag des Kaufs |

> Auf Basis dieser Spalten werden die KPIs (Ranking etc.) berechnet.

---

### 📅 Zeitraum / Scope / Darstellung

| Kategorie | Entscheidung / Einschränkung |
|----------|------------------------------|
| Zeitraum | **letzte 12 Monate (rolling)** |
| Kundenscope | **nur Kunden des Account Managers** |
| Segmentierung | keine Gruppierung notwendig (einfache Liste reicht) |
| Darstellung | einfache Tabelle + Ranking |
| Visualisierung | nicht erforderlich / optional später |

---

### 📁 Format / Output

| Output | Details |
|--------|---------|
| ✅ Excel Datei | monatlich aktualisierbar, als Ergebnis für den Stakeholder |
| ➕ optional (future) | Power BI Self-Service Dashboard für Automatisierung |

> Visualisierung ist **nicht entscheidend** – wichtiger sind korrekte KPIs und Logik.  
> Visualisierung = Transportmittel.

---

### 🔌 Datenquelle / technische Rahmenbedingungen

- Daten stammen aus dem **ERP-System**.
- Export erfolgt **monatlich als Excel/CSV**.
- **Kein direkter Zugriff** auf ERP/DB für Analysten.
- Aktualisierung erfolgt durch **Ersetzen der Exportdatei**.
- Report wird so aufgebaut, dass alle Berechnungen **automatisch aktualisiert** werden (Power Query / Power BI / Excel Automations).
- Für später wäre eine direkte Datenanbindung (z. B. BI / API / Datenbank) sinnvoll, aber **nicht Teil des aktuellen Scopes**.

---

### ✅ Definition of Done

Der Report gilt als „fertig“, wenn:

- Excel enthält alle relevanten Kunden (nur Kunden des AM)
- Zeitraum = letzte 12 Monate
- KPIs:
  - letzter Kaufzeitpunkt
  - Anzahl Aufträge
  - Umsatz
  - Ranking
  - Inaktivitätsflag
- Datei kann **monatlich aktualisiert werden, ohne dass Formeln neu gebaut werden müssen**

---

### 🔁 Iterative Zusammenarbeit

- Stakeholder kann nach dem ersten Ergebnis zusätzliche Anforderungen einbringen.
- Follow-up nach erster Version eingeplant.

> „Wenn du magst, kann ich dir die Spalten später nochmal genau aufschreiben.“

---