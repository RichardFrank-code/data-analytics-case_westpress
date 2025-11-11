# Analyst Notes & Open Questions

> 🧠 Dieses Dokument sammelt laufend offene Fragen, Beobachtungen und Hypothesen während der Analyse.  
> Ziel ist, die Kommunikation mit Stakeholdern (z. B. fiktivem Mitarbeiter / Chatbot) zu dokumentieren  
> und den Gedankengang nachvollziehbar zu halten.

---

## 🔍 Offene Fragen

### BC_NUMBER
- Bedeutung unklar – steht vermutlich für **Booking Confirmation Number** oder **Business Case Number**?  
- Besteht aus numerischem Teil + Suffix (`A0–A9`) → evtl. Unterversion oder Teilauftrag.  
- Frage: Wird `BC_NUMBER` in allen Datensätzen konsistent genutzt und ist sie eindeutig?

---

### Datenqualität & Tracking
- Bei einigen `SUPPLIER`-Daten fehlen `DATE`-Werte → sind das bekannte Systemlücken oder temporäre Fehler?  
- Gibt es definierte Qualitätsgrenzen, ab wann eine Quelle ausgeschlossen werden sollte?

---

### Weitere Beobachtungen / Hypothesen
- `missing_pct` bei großen Lieferanten ist gering, aber absolut relevant.  
- Potenzielle Fallstricke: doppelte IDs, uneinheitliche Spaltennamen, nicht synchronisierte Zeiträume.
