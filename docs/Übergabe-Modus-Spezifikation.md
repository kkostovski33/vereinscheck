# VereinsCheck – Übergabe-Modus (Spezifikation v0.1)

*Stand: 21.09.2026 · Innovationskern für Prototype-Fund-Bewerbung*  
*Status: Konzept — Wireframe folgt (Person D, Deadline 27.09.)*

> **Kernversprechen:** IT-Wissen übersteht den Vorstandswechsel. Das unterscheidet VereinsCheck von jedem Header-Scanner.

---

## Problem

Typischer Satz nach jedem Vorstandswechsel: *„Wir wissen nicht mehr, wer die Domain verwaltet."*

Technische Scans (A–H) sehen nur die Website. Sie sehen nicht:
- wer Zugänge hat (und wer sie noch hat)
- wo die Mitgliederliste liegt
- wer die Rechnung für Hosting zahlt

---

## Lösung: Drei Bausteine

### 1. Scan-Ergebnis (automatisch)
Bestehende Checks A–F aus dem Prüfkatalog → PDF-Inventar

### 2. Geführter Dialog (Abschnitt I)
10–15 Fragen in Vereinssprache → Zugriffs- und Verantwortlichkeitsregister

**Fragen (Entwurf):**

1. Wer hat heute Zugang zum Website-Verwaltungsbereich? (Namen, nicht Rollen)
2. Wer hatte früher Zugang und hat ihn eventuell noch?
3. Auf wen läuft der Vertrag für Domain und Hosting? Wer zahlt die Rechnung?
4. Wo liegt die Mitgliederliste? (Vereinssoftware, Excel, Cloud, Papier)
5. Wer hat Zugriff auf das Vereinspostfach?
6. Wer hat Zugriff auf das Vereinskonto und das Spendentool?
7. Werden Mitgliederdaten über WhatsApp oder private Mailadressen ausgetauscht?
8. Gibt es Backups? Wer prüft, ob sie funktionieren?
9. Welche Dienstleister verarbeiten Daten für euch?
10. Was passiert beim nächsten Vorstandswechsel mit all dem?

**Datenschutz:** Verarbeitung nur im Browser, Ausgabe als PDF, **keine Serverspeicherung**.

### 3. Übergabe-Modus (Abschnitt J)
Aktivierbarer Zusatzmodus „Der Vorstand wechselt":

- Checkliste zum Entzug der Zugänge ausscheidender Personen (pro Dienst)
- Hinweise zu Vertragsüberschreibung (Domain, Hosting, Vereinssoftware)
- **Übergabemappe als PDF:** Inventar (F) + Zugriffsregister (I) + offene Befunde + Prüfdatum + Unterschriftenfelder
- Wiedervorlage: Erinnerung zur erneuten Prüfung nach 12 Monaten

---

## User Flow (Wireframe-Grundlage)

```
[Start] → Website scannen → Ampel-Ergebnis
                ↓
         „Vorstand wechselt bald?"
                ↓ Ja
         Geführter Dialog (10 Fragen)
                ↓
         Übergabemappe generieren (PDF)
                ↓
         Entzugs-Checkliste pro Dienst
```

---

## Wireframe — TODO

- [ ] `[PLATZHALTER Person D]` — 3 Screens: Scan-Ergebnis → Dialog → PDF-Vorschau
- [ ] Export als PNG für Bewerbungs-Anhang (Deadline: 15.10.)

---

## Bezug zum Prüfkatalog

| Prüfkatalog | Übergabe-Modus |
|---|---|
| F — Domain-Inventar | Automatisch im Scan |
| I — Geführter Dialog | Kern des Modus |
| J — Übergabe-Modus | PDF + Entzugs-Checkliste |

---

## Was für die Bewerbung reicht

- Diese Spezifikation ✅
- Wireframe/Mockup (3 Screens) — noch offen
- **Nicht nötig vor Submit:** Implementierung (Förder-Meilenstein M4)
