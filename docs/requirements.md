# R# Requirements – Stakeholder-Chat

## Ziel des Gesprächs
Die Anforderungen für einen **automatisierten, regelmäßigen Performance-Report** zu Stellenanzeigen erfassen,
inkl. Datenquellen, KPIs, Empfänger:innen, Frequenz und aktueller Entscheidungsgrundlage.

## Kontext (aus Aufgabe)
- Abteilung bevorzugt **automatisierte Berichte** (statt manueller Analysen)
- Datenquellen: `Umsatzdaten.xlsx` + `Trackingdaten.xlsx`
- Ziel: Ableitung von Insights für optimierte Entscheidungen im Anzeigen-Management
- Präsentation der Ergebnisse: **Freitag 15:00 Uhr**

---

## Leitfragen (duzen)

### 1) Ziel & Entscheidung
- Was möchtest du mit dem Report entscheiden?
- Wer nutzt den Report (Zielgruppe)?
- Welche Entscheidungen beeinflusst der Report? (Budget, Laufzeit, Kanalwahl)

### 2) KPIs (Definitionen explizit fixieren)
- Primäre KPIs: Umsatz, Klicks, Bewerbungen, Conversion Rate, **Cost per Application (CPA)**, **Preis/Leistung**
- Wie definieren wir „Bewerbung“ genau? (Event? Status?)
- Gibt es interne Zielwerte / Benchmark-Grenzen?

### 3) Dimensionen / Segmentierung
- Nach welchen Achsen willst du vergleichen?
  (Job-Typ/Branche, Stellenbörse, Kunde, Zeitraum, Region, Kampagne…)
- **Soll es Drilldowns geben?** (z. B. von Gesamt → Kunde → Anzeige)

### 4) Frequenz & Automatisierung
- Wie oft soll der Report aktualisiert werden? (täglich / wöchentlich / monatlich)
- In welchem Format willst du ihn konsumieren? (Dashboard, Excel, PDF)
- Sollen Benachrichtigungen / Alerts bei Auffälligkeiten gesendet werden?

### 5) Datenquellen & Join
- Wie werden Umsatz- und Trackingdaten verknüpft? (gemeinsamer Schlüssel?)
- Gibt es Datenpunkte, die aktuell fehlen oder manuell ergänzt werden müssen?
- **Wie groß ist der zeitliche Verzug der Daten?** (z. B. Reporting-Day + 1)

### 6) Klassifikation Job/Branche
- Welche Kategorien oder Taxonomien sollen verwendet werden?
- Gibt es bestehende Zuordnungen / Vorlagen?

### 7) Leistungsbewertung / Score (Reporting-Logik)
- Woran erkennst du eine „gute“ Anzeige?
  (z. B. Bewerbungen >= X, CPA <= Y, ROI >= Z)
- **Soll es eine Ampel- oder Score-Darstellung geben?**

### 8) Akzeptanzkriterien (Definition of Done)
- Was muss enthalten sein, damit der Report für dich „fertig und produktiv nutzbar“ ist?
- Was wäre „Nice to Have“, aber nicht notwendig?

---

## Gesprächsnotizen (werden während des Chats ergänzt)

- **[YYYY-MM-DD HH:MM] Du:** …
- **[YYYY-MM-DD HH:MM] Stakeholder:** …
- **Kurzfassung:** …

---

## Zusammenfassung der Anforderungen (nach dem Chat)

| Kategorie | Ergebnis |
|----------|----------|
| Ziel | … |
| KPIs | … |
| Segmente | … |
| Frequenz | … |
| Format | … |
| Definition of Done | … |
| Offene Punkte | … |

