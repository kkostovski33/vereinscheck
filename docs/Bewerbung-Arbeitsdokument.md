# VereinsCheck – Prototype Fund Bewerbung (Arbeitsdokument)

*Stand: 21.09.2026 · Zum Kopieren ins Portal ab 01.10.2026*  
*Förderschwerpunkt: **Datensicherheit** · Förderlinie: Innovation · GitHub: https://github.com/kkostovski33/vereinscheck*

> **Anleitung:** Felder mit `[PLATZHALTER]` vom Team befüllen. Fertige Textblöcke aus [`Prototype-Fund-Bewerbung-Bausteine.md`](./Prototype-Fund-Bewerbung-Bausteine.md) sind bereits eingefügt. Zeichenlimit pro Feld: ~2.000.

---

## Status-Tracker

| Bereich | Status |
|---|---|
| Kern-Antworten (3× ~2.000 Zeichen) | ✅ Text vorhanden |
| Meilensteine / Arbeitsplan | ✅ Text vorhanden |
| Team-Namen & Profile | ❌ `[PLATZHALTER]` |
| GF + Freistellungsplan | ❌ `[PLATZHALTER]` |
| Kooperationspartner / LOI | ⏳ DsiN/BBE angefragt, Antwort offen |
| Anhänge (Prüfkatalog, Wireframe, Fallstudien) | ❌ noch anlegen |
| Second Stage | ✅ Text vorhanden |

**Team-Deadline für Platzhalter:** Mittwoch, 24.09.2026

---

## Team

| Rolle | Name | Wohnort | Stunden (6 Mon.) | Kurzprofil |
|---|---|---|---|---|
| Person A — GF, Vollzeit | `[PLATZHALTER]` | `[PLATZHALTER]` DE | 950 Std. | `[PLATZHALTER]` |
| Person B — Engine | `[PLATZHALTER]` | `[PLATZHALTER]` | ~317 Std. | `[PLATZHALTER]` |
| Person C — Frontend | `[PLATZHALTER]` | Deventer, NL | ~317 Std. | `[PLATZHALTER]` |
| Person D — Übergabe/UX | `[PLATZHALTER]` | Deventer, NL | ~317 Std. | `[PLATZHALTER]` |

**GbR:** Gründung erst nach Förderzusage (~Ende Jan. 2027). Sitz: `[PLATZHALTER]` (DE).

**Persönliche Motivation (Vereinsbezug):** `[PLATZHALTER — mindestens 1 Person mit erster Hand-Erfahrung]`

**Freistellung Person A ab 01.06.2027:** `[PLATZHALTER — Arbeitgeber, Umfang, geklärt ja/nein]`

---

## Feld 1: Projekt kurz beschreiben (~2.000 Zeichen)

```
VereinsCheck ist ein kostenloses, quelloffenes Werkzeug, mit dem gemeinnützige 
Vereine die IT-Sicherheit ihrer Website in unter zwei Minuten selbst prüfen 
können – ohne technisches Vorwissen und ohne Fachjargon.

Rund 600.000 Vereine in Deutschland werden ehrenamtlich geführt. Ihre Vorstände 
wechseln oft alle ein bis zwei Jahre, und mit jedem Wechsel geht IT-Wissen verloren: 
Niemand weiß mehr, wer die Domain verwaltet, ob das Verschlüsselungs-Zertifikat 
noch gültig ist oder ob das Spendenformular datenschutzkonform gebaut wurde. 
Bestehende Prüf-Werkzeuge (z. B. Mozilla Observatory, SSL Labs) richten sich 
an Entwickler*innen und liefern technische Rohdaten ohne Handlungsplan.

VereinsCheck schließt diese Lücke: Der Verein gibt seine Website-Adresse ein 
und erhält eine verständliche Ampel-Bewertung (grün/gelb/rot) zu vier Bereichen: 
HTTPS-Verschlüsselung, Security-Header, Tracking & Cookies sowie die Sicherheit 
von Spenden- und Mitgliedsformularen. Jedes Ergebnis wird in Klartext erklärt 
und mit konkreten „Was kann ich tun?"-Schritten versehen.

Das Alleinstellungsmerkmal ist die übergabefähige Dokumentation: ein geführter 
Dialog und eine Checkliste, die der scheidende Vorstand ausfüllt und an den 
Nachfolger weitergibt – damit IT-Wissen den Vorstandswechsel übersteht. VereinsCheck 
prüft also nicht nur, sondern adressiert das strukturelle Ehrenamts-Problem.

Ein funktionierender Open-Source-Prototyp (Version 0.3.0) mit Scan-Engine, 
Web-Oberfläche und PDF-Bericht ist unter github.com/kkostovski33/vereinscheck 
öffentlich verfügbar. VereinsCheck speichert keine Nutzerdaten – jeder Scan 
wird im Arbeitsspeicher verarbeitet und verworfen.

Ziel der Förderphase: Aus dem Prototyp ein robustes, laienfreundliches Werkzeug 
machen, den Prüfkatalog schrittweise umsetzen (v1.0: 7 Prüfbereiche A–F plus 
Übergabe-Modus I/J) und über Dachverbände in die Breite tragen.
```

---

## Feld 2: Meilensteine / Was passiert in 6 Monaten? (~2.000 Zeichen)

```
Aufbauend auf dem vorhandenen Prototyp (v0.3.0, GitHub) gliedert sich die 
sechsmonatige Förderphase in Arbeitspakete für das vierköpfige Team:

Monat 1–2 – Engine härten + erste Erweiterungen:
Unit-/Integrationstests (pytest) für alle Checks. Scan-Logik anhand 
mindestens 50 realer Vereins-Websites verfeinern. Fehlertoleranz bei 
Redirects und gemischten HTTP/HTTPS-Setups. Schnellgewinn C6/C7: 
Impressum- und Datenschutzerklärungs-Erkennung (HTML). Bewertungslogik 
Security-Header entschärfen (gelb statt Panik-Rot bei kleinen Vereinen).

Monat 2–3 – Datensicherheits-Kern (Prüfkatalog E + D + F):
Neues Modul E-Mail-Identität (SPF, DMARC, DKIM, MX — Schutz vor 
gefälschten Vorstands-Mails). Formular-Check auf D1–D10 ausbauen 
(GET statt POST, Tracker auf Spendenseite, Zahlungsdienst-Einordnung). 
Domain-/Hosting-Inventar (Registrar, Ablaufdatum, Serverstandort). 
PDF plattformunabhängig (Linux-Server).

Monat 3–4 – Übergabe-Werkzeug (Prüfkatalog I + J — Alleinstellungsmerkmal):
Geführter Dialog (10–15 Fragen in Vereinssprache) → Zugriffsregister 
(Art.-30-nahe Übersicht, nur im Browser, kein Server-Speicher). 
Übergabe-Modus: Entzugs-Checkliste pro Dienst, PDF-Übergabemappe 
(Scan-Inventar + Dialog + offene Befunde + Unterschriftenfelder). 
Usability-Test mit 3 Vereinsvorständen.

Monat 4–5 – Prüftiefe & Nutzererfahrung:
Browser-basierte Tracking-Prüfung (Playwright, C1–C5 — grau statt grün 
wenn nicht prüfbar). SSL-Ergänzungen A4–A7. WCAG 2.1 AA Basics 
(Mobile, Tastatur, Kontrast). Lösungsdatenbank: 20 Starteinträge mit 
anbieterspezifischen Klickpfaden (WordPress, IONOS, Strato, Twingle …). 
Praxistests mit 5–10 Vereinen.

Monat 5–6 – Verbreitung & Nachhaltigkeit:
Pilot mit mindestens einem Dachverband. Self-Hosting-Doku für Verbände. 
Öffentliches Hosting unter vereinscheck.de. Veröffentlichung v1.0 
(7 Prüfbereiche: A–F automatisch + Dialog/Übergabe I/J).

Meilensteine: M2 = getestete Engine + Impressum/DSE; M3 = E-Mail-, 
Formular- und Domain-Checks; M4 = Übergabe-Modus; M5 = Browser-Tracking 
+ Praxistests; M6 = v1.0 live mit Verbandspilot.
```

> **Feature-Tiers:** Vollständige Priorisierung → [`Prototype-Fund-Bewerbung-Bausteine.md`](./Prototype-Fund-Bewerbung-Bausteine.md) §16

---

## Feld 3: Zielgruppe & wie erreicht ihr sie? (~2.000 Zeichen)

```
Zielgruppe: Die rund 600.000 ehrenamtlich geführten Vereine in Deutschland – 
insbesondere kleine und mittlere Vereine ohne IT-Abteilung, deren Vorstände 
die Website „nebenbei" betreuen.

Erreichung über Multiplikatoren, nicht Einzelansprache:
- Dachverbände und Engagement-Netzwerke (DsiN/Digitale Nachbarschaft, 
  BBE – Bundesnetzwerk Bürgerschaftliches Engagement, DSEE)
- Kooperationsanfragen versendet (Stand 04.09.2026), Antworten noch offen:
  DsiN (info@sicher-im-netz.de), BBE (info@b-b-e.de)
  [PLATZHALTER: LOI-Status bis 15.10. eintragen]
- Fallback: Landessportbund + 5–10 benannte Praxistest-Vereine
- Open Source: Verbände können VereinsCheck einbinden und dauerhaft betreiben

Erfolgsmessung:
- Anzahl gescannter Vereins-Websites (anonym)
- Anzahl eingebundener Verbände/Pilotpartner
- Anzahl generierter Übergabe-Mappen (Download-Zähler)
- Qualitative Rückmeldungen aus Praxistests

Langfristig: VereinsCheck als dauerhaftes, kostenloses Werkzeug in der 
Vereins-Infrastruktur. Kein Abo-Modell, keine Datensammlung.
```

---

## Weitere Portal-Felder (Entwurf)

### Gesellschaftliche Herausforderung

→ Volltext in Bausteine §2 (oben kopieren bei Bedarf)

### Technische Umsetzung

→ Volltext in Bausteine §3

### Bisherige Vorarbeit

- v0.3.0: 4 Checks, Flask-UI, PDF, Formular-Check, Datenschutz-by-Design
- Prüfkatalog v0.1 (10 Bereiche A–J)
- GitHub: https://github.com/kkostovski33/vereinscheck

### Abgrenzung zur Konkurrenz

- SIWECOS (eingestellt 06/2026), WebPrüfer, Mozilla Observatory — ehrlich benennen
- VereinsCheck: Übergabe-Modus, Formular-Fokus, Vereinssprache, Privacy-by-Design

### Second Stage (mit beantragen)

```
User Tests über Dachverbände, Öffentlichkeitsarbeit, Community für Lösungsdatenbank,
WordPress-Plugin als Verbreitungskanal, Hosting durch Verbände (kein SaaS-Zwang),
Prüfkatalog G/H vorsichtig ausbauen.
```

---

## Budget

| | Stunden | Budget |
|---|---|---|
| Person A (GF, Vollzeit) | 950 | 47.500 € |
| Person B + C + D | 950 | 47.500 € |
| **Gesamt** | **1.900** | **95.000 €** |
| + 5 % Gemeinkosten | | **99.750 €** |

---

## Anhänge (noch anlegen)

- [ ] `docs/Pruefkatalog-v0.1.md` (aus Upload)
- [ ] `docs/Übergabe-Modus-Spezifikation.md` + Wireframe PNG
- [ ] `docs/fallstudien/` — 3–5 Scan-Screenshots mit Kurztext
- [ ] `[PLATZHALTER]` LOI von DsiN/BBE/Landessportbund (falls vorhanden)

---

## Praxistest-Vereine

| # | Verein | URL | Ansprechpartner | Status |
|---|---|---|---|---|
| 1 | `[PLATZHALTER]` | `[PLATZHALTER]` | `[PLATZHALTER]` | |
| 2 | `[PLATZHALTER]` | `[PLATZHALTER]` | `[PLATZHALTER]` | |
| 3 | `[PLATZHALTER]` | `[PLATZHALTER]` | `[PLATZHALTER]` | |

---

## Submit-Checkliste

Siehe [`Prototype-Fund-Bewerbung-Bausteine.md`](./Prototype-Fund-Bewerbung-Bausteine.md) §12 und [`Prototype-Fund-Startplan.md`](./Prototype-Fund-Startplan.md).

**Submit bis spätestens 28.11.2026** (Puffer vor 30.11.).
