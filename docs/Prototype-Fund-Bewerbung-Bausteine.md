# VereinsCheck – Bewerbungsbausteine Prototype Fund

*Aktualisierter Stand: 21.09.2026 – integriert: Kristijans Uploads (Fortschritt 04.09., Förder-Zusammenfassung 28.08., README, requirements)*

> **Bewerbungsfenster Jahrgang 03:** 01.10.–30.11.2026 · Förderstart 01.06.2027 · 6 Monate (+ optional 4 Monate Second Stage)  
> **Förderschwerpunkt wählen:** Datensicherheit (Förderlinie Innovation)  
> **GitHub:** https://github.com/kkostovski33/vereinscheck (v0.3.0)

---

## Strategie in drei Sätzen

1. **Nicht** als „noch ein Security-Scanner“ positionieren, sondern als **Public-Interest-Tool für 600.000 ehrenamtlich geführte Vereine**.
2. **Kern-Innovation:** Übergabe-Werkzeug (Prüfkatalog Abschnitt I + J) — IT-Wissen übersteht den Vorstandswechsel.
3. **Förderphase rechtfertigen:** Prototyp läuft (4 Checks, Web-UI, PDF); Förderung finanziert Robustheit, E-Mail-/Formular-Checks, Dialog/Übergabe-Modus, Praxistests, Verbands-Rollout.

---

## 1. Projektziel / Kurzbeschreibung *(~2.000 Zeichen)*

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

## 2. Gesellschaftliche Herausforderung *(~2.000 Zeichen)*

```
Datensicherheit im Ehrenamt ist ein strukturelles, wiederkehrendes Problem – 
noch ohne passende Lösung.

Über 600.000 Vereine in Deutschland verarbeiten sensible personenbezogene Daten: 
Mitgliedslisten mit Namen und Adressen, Spender-IBANs, Geburtsdaten bei 
Jugendangeboten. Die meisten betreiben ihre Website nebenbei, ohne IT-Fachkenntnisse 
und ohne Budget für externe Beratung. Sicherheitslücken – abgelaufene Zertifikate, 
fehlende Verschlüsselung bei Formularen, Tracking ohne Einwilligung – bleiben 
unbemerkt, bis Mitgliederdaten kompromittiert sind oder Abmahnungen drohen.

Verschärft wird das durch die hohe Fluktuation im Ehrenamt: Vorstände wechseln 
regelmäßig, Wissen über Hosting-Zugänge, Domain-Inhaberschaft und Sicherheitsstand 
wird selten dokumentiert und geht beim Wechsel verloren. Der neue Vorstand startet 
blind – und das Problem wiederholt sich alle ein bis zwei Jahre.

Bestehende Security-Tools adressieren dieses strukturelle Problem nicht: Sie 
prüfen technisch korrekt, sprechen aber Fachsprache, liefern keine Handlungsempfehlungen 
für Laien und bieten keine Möglichkeit, Erkenntnisse an den nächsten Vorstand 
weiterzugeben. Seit der Abschaltung von SIWECOS (Juni 2026) fehlt zudem ein 
kostenloser, verständlicher Sicherheits-Check für den deutschsprachigen Raum.

VereinsCheck adressiert beides: Es macht grundlegende IT-Sicherheit für 
Vereinsvorstände ohne Fachwissen zugänglich und schafft mit dem Übergabe-Modus 
eine dokumentierte Wissensbasis, die den Vorstandswechsel überdauert. So werden 
ehrenamtlich geführte Organisationen befähigt, die Daten ihrer Mitglieder und 
Spender selbst zu schützen – unabhängig von kommerziellen Beratungsangeboten.
```

---

## 3. Technische Umsetzung *(~2.000 Zeichen)*

```
VereinsCheck ist als modulares Python-Projekt aufgebaut (MIT-Lizenz, GitHub).

Architektur:
- Scan-Engine (Python 3.10+): Vier unabhängige Prüfmodule in checks/ – 
  ssl_check (TLS-Zertifikat), headers_check (5 Security-Header), 
  tracking_check (heuristische Tracker-/Consent-Erkennung), form_check 
  (sensible Formularfelder, HTTPS/POST, DSGVO-Einwilligung).
- Web-Frontend: Flask-App mit serverseitigem Scan, Ampel-Darstellung, 
  Handlungsempfehlungen mit Code-Snippets (.htaccess, nginx, WordPress).
- PDF-Bericht: fpdf2, weiterleitbar an Webmaster.
- Datenschutz: Keine Datenbank, kein Logging von URLs/Ergebnissen/IP-Adressen.

Fachliche Spezifikation: Ein Prüfkatalog (10 Bereiche A–J) definiert, was geprüft 
wird, wie bewertet wird und welche Handlung folgt. Leitprinzipien: Vereinssprache 
vor Fachsprache, kein Befund ohne Handlung, nur passive Prüfungen, Grau nie 
still zu Grün.

Geplante Erweiterungen in der Förderphase (Priorität laut Prüfkatalog, siehe §16):
- Tier 1: E (E-Mail-Identität), D (D1–D10), F (Domain-Inventar), I+J (Übergabe),
  C6/C7 (Impressum/DSE), Lösungsdatenbank, pytest
- Tier 2: C1–C5 (Playwright), A4–A7 (SSL-Tiefe), WCAG, Verbandspilot
- Tier 3 (Second Stage): G (Software-Aktualität), H (Datenspuren), WP-Plugin

Technologie-Stack: Python, Flask, BeautifulSoup4, requests, fpdf2, pytest, 
optional Playwright. Keine proprietären Abhängigkeiten. Modulare Struktur 
ermöglicht parallele Entwicklung und spätere Erweiterung durch Dachverbände.
```

---

## 4. Meilensteine / Arbeitsplan *(~2.000 Zeichen)* — KORRIGIERT

> **Wichtig:** PDF-Bericht ist in v0.3.0 bereits umgesetzt. Nicht als Neuentwicklung planen.

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

---

## 5. Zielgruppe & Erreichung *(~2.000 Zeichen)*

```
Zielgruppe: Die rund 600.000 ehrenamtlich geführten Vereine in Deutschland – 
insbesondere kleine und mittlere Vereine ohne IT-Abteilung, deren Vorstände 
die Website „nebenbei" betreuen.

Erreichung über Multiplikatoren, nicht Einzelansprache:
- Dachverbände und Engagement-Netzwerke (DsiN/Digitale Nachbarschaft, 
  BBE – Bundesnetzwerk Bürgerschaftliches Engagement, DSEE)
- Kooperationsanfragen **versendet** (Stand 04.09.2026), Antworten noch offen:
  - **DsiN / Digitale Nachbarschaft:** info@sicher-im-netz.de
    (Ausweich von dina@digitale-nachbarschaft.de — Adresse technisch defekt)
  - **BBE:** info@b-b-e.de
  - Inhalt: Projekt-Vorstellung, GitHub-Link, Bitte um 15–20-Min-Gespräch 
    und schriftliche Interessensbestätigung für Testphase mit Mitgliedsvereinen
  - **Fallback bei Ablehnung/keine Antwort:** weitere Dachverbände (z. B. Landessportbund)
- Open Source ermöglicht Verbänden, VereinsCheck auf eigenen Seiten 
  einzubinden und dauerhaft weiterzubetreiben – unabhängig vom Kernteam

Erfolgsmessung:
- Anzahl gescannter Vereins-Websites (anonym, ohne Speicherung)
- Anzahl eingebundener Verbände/Pilotpartner
- Anzahl generierter Übergabe-Mappen (Download-Zähler)
- Qualitative Rückmeldungen aus Praxistests (Protokolle)

Langfristig: VereinsCheck als dauerhaftes, kostenloses Werkzeug in der 
Vereins-Infrastruktur – vergleichbar mit Impressum-Generatoren, aber 
für IT-Sicherheit. Kein Abo-Modell, keine Datensammlung.
```

---

## 6. Bisherige Vorarbeit / geplante Neuerungen

**Bereits umgesetzt (Open Source, v0.3.0):**
- Vier funktionierende Prüfmodule mit Ampel-Ausgabe und Handlungsempfehlungen
- Lauffähige Web-Oberfläche (Flask) mit PDF-Export
- Datenschutzerklärung (privacy-by-design: keine Datenspeicherung)
- Prüfkatalog v0.1 als fachliche Spezifikation (10 Bereiche A–J)
- Erfolgreich getestet an echten Vereins-Websites
- Formular-Check umgesetzt (Erkennung sensibler Felder, HTTPS/GET/POST, 
  DSGVO-Einwilligung, Drittanbieter-Einbettung) — war geplant ab 05.09.2026

**Formular-Check — geplante Aufgabenteilung (4 Personen, aus Konzept 04.09.):**
1. Person B: Formular-Erkennung (BeautifulSoup) + Zusammenführung aller Teilergebnisse
2. Person C: Übertragungsweg-Check (HTTPS/GET/POST)
3. Person D: Datenschutz-Einwilligung-Heuristik
4. Person A: Drittanbieter-Check + Praxistest gegen 5–10 echte Vereins-Websites

**Geplant in der Förderphase (Tier 1 + 2, siehe §16):**
1. **Tier 1:** E-Mail-Identität (E), Formular D1–D10 (D), Domain-Inventar (F), Dialog (I), Übergabe (J), Impressum/DSE (C6/C7), Lösungsdatenbank, pytest
2. **Tier 2:** Browser-Tracking (C1–C5), SSL A4–A7, WCAG, Praxistests, Verbandspilot
3. **Tier 3 (Second Stage):** Software-Aktualität (G), Datenspuren (H), WordPress-Plugin

---

## 7. Abgrenzung zur Konkurrenz

| Tool | Schwäche für Vereine | VereinsCheck-Vorteil |
|---|---|---|
| **SIWECOS** (eingestellt 06/2026) | Fachlich, kein Vereins-Kontext | Vereinssprache, Formular-Fokus, Übergabe-Modus |
| **WebPrüfer** | Breit für Unternehmen, kein Vorstandswechsel-Modul | Schmaler Fokus + Wissensübergabe |
| **Mozilla Observatory / SSL Labs** | Englisch, Entwickler-Zielgruppe | Deutsch, Ampel, Handlungsschritte |
| **Monolox o.ä.** | Bezahlt, technisch | Kostenlos, Open Source, ehrenamtlich nutzbar |

**Drei Alleinstellungsmerkmale:**
1. **Übergabe-Modus** (Prüfkatalog J) — dokumentierte Wissensbasis beim Vorstandswechsel
2. **Formular-Check D1–D10** — sensible Vereinsdaten, Tracker auf Spendenseite
3. **E-Mail-Identität E1–E7** — Schutz vor gefälschten Vorstands-Mails (CEO-Fraud im Ehrenamt)
4. **Privacy-by-Design** — kein Tracking, keine Datenspeicherung beim Scanner selbst

---

## 8. Second Stage (4 Monate — mit beantragen)

```
In den 4 Monaten nach dem Prototyp:
- User Tests mit Vereinen über Dachverbände (DsiN, BBE, DSEE)
- Öffentlichkeitsarbeit (Verbandstage, DsiN-Materialien)
- Aufbau einer Community für Wartung der Lösungsdatenbank
- WordPress-Plugin als Verbreitungskanal
- Nachhaltigkeitskonzept: Hosting durch Verbände, kein SaaS-Zwang
- Prüfkatalog-Bereiche G (Aktualität) und H (Datenspuren) vorsichtig ausbauen
```

---

## 9. Prüfkatalog — Stärke für die Bewerbung

Der Prüfkatalog zeigt der Jury **inhaltliche Tiefe**, nicht nur eine Idee:

| Bereich | Inhalt | Stand v0.3.0 | Förder-Priorität |
|---|---|---|---|
| **A** | HTTPS/Verschlüsselung | ✅ Grundlage | A4–A7 ergänzen |
| **B** | Security-Header | ✅ vorhanden | Bewertung entschärfen |
| **C** | Tracking/Einwilligung | ✅ heuristisch | Browser-Prüfung C5–C7 |
| **D** | Formular-Sicherheit | ✅ Grundlage | **D1–D10 — Kern** |
| **E** | E-Mail-Identität (SPF/DMARC) | ❌ offen | **Schnell, hoher Wert** |
| **F** | Domain-/Hosting-Inventar | ❌ offen | Übergabe-Story |
| **G** | Software-Aktualität | ❌ offen | Second Stage |
| **H** | Datenspuren (PDF-Listen) | ❌ offen | Second Stage, vorsichtig |
| **I** | Geführter Dialog / Zugriffsregister | ❌ offen | **Innovationskern** |
| **J** | Übergabe-Modus | ❌ offen | **Innovationskern** |

**Leitprinzipien (für Jury betonen):**
- Vereinssprache vor Fachsprache
- Kein Befund ohne Handlung (anbieterspezifische Klickpfade)
- Nur passive Prüfungen (rechtliche Leitplanken)
- Grau nie still zu Grün (ehrliche Bewertung)

---

## 10. Team, Budget & Formalien

### Team (fest, 4 Personen)

- **4 IT-Ingenieur:innen**, davon **2 in Deventer (Niederlande)** — EU-Ausland ist beim Prototype Fund zulässig
- Alle Teammitglieder stehen fest; modulare Code-Struktur ist auf arbeitsteiliges Arbeiten ausgelegt
- **Antragsteller:** Team (max. 4 Personen), **nicht** als Verein — Pflicht ist eine **GbR mit Sitz in Deutschland**
- **GbR-Gründung:** erst **nach Förderzusage** (voraussichtlich Ende Januar 2027), nicht vor der Bewerbung
- Geschäftsführer:in mit Wohnsitz in DE; Open Source (MIT ✅)
- **Parallel:** e.V.-Gründung mit 7 Gründungsmitgliedern läuft separat (ab 01.08.2026 geplant) — unabhängig vom PF-Zeitplan, da PF keine Vereinsregistrierung verlangt

| Person | Rolle (Vorschlag) | Arbeitspaket | Standort |
|---|---|---|---|
| Person A (DE, GF, Vollzeit) | Projektleitung, Verbands-Kontakte, GbR | M5–M6 | Deutschland |
| Person B | Scan-Engine, Tests, Formular-Check | M1–M3 | — |
| Person C | Frontend, Barrierefreiheit | M4–M5 | Deventer (NL) |
| Person D | Übergabe-Modus, UX-Texte, Prüfkatalog | M3–M4 | Deventer (NL) |

### Budget-Mechanik (Prototype Fund / „Software Sprint", BMFTR via OKF)

| Parameter | Wert |
|---|---|
| Bewerbungsfenster | 01.10.–30.11.2026 |
| Erfolgsquote | ca. 8 % (25–30 von zuletzt ~327 Bewerbungen) |
| Auswahl | komplett schriftlich, **kein Pitch** in Stage 1 |
| Team-Maximum | 1.900 Std. / **95.000 €** (+ 5 % Gemeinkosten) |
| Einzelperson-Maximum | 950 Std. / 50.000 € |
| Förderstart (bei Zusage) | fix **01.06.2027**, 6 Monate |
| Erste Auszahlung | nach Monat 1 (Juni/Juli 2027) |
| Second Stage (optional) | Dez. 2027 – März 2028, +63.333 € Team (mit Jury-Präsentation) |

**Geplante Stunden-Konstellation (realistisch volle 95.000 €):**

| Person | Modell | Stunden | Budget |
|---|---|---|---|
| Person A (GF) | Vollzeit-Freistellung vom Hauptjob | 950 Std. | 47.500 € |
| Person B + C + D | je ca. 12 Std./Woche (Teilzeit/Minijob) | zusammen 950 Std. | 47.500 € |
| **Gesamt** | | **1.900 Std.** | **95.000 €** |

→ Plus 5 % Gemeinkosten = **99.750 €** Gesamtförderung.  
→ **Arbeitszeitgesetz:** Hauptjob + PF-Arbeit zusammen max. **48 Std./Woche** pro Person.

### Parallele Förderstrategie (ohne Doppelförderung)

- **Kooperationspartner** (DsiN, BBE, Landessportbund …): unbegrenzt parallel anfragbar
- **Weitere Förderprogramme** parallel erlaubt, solange keine Doppelförderung exakt gleicher Kosten:
  - **DSEE** (Digitalisierung im Ehrenamt) — Fördermittelwerkstatt Okt./Nov. 2026 als Einstieg
  - **NLnet Foundation** (Open Source, Sitz NL) — passt zum Team-Standort Deventer
- **Erasmus+** (MitWirkung/KA154) — zweitrangig, seit PF-Fokus

### Verworfene Projektalternativen (für Jury-Kontext)

- Barrierefreie UI-Bibliothek — Markt zu gesättigt
- Stalkerware-Detector — technisches Risiko zu hoch für Erstlings-Team

---

## 11. Schwächen & Gegenmaßnahmen

| Schwäche | Gegenmaßnahme |
|---|---|
| Keine LOI von Verbänden | Bis 30.11. Antworten einholen; 2–3 Vereine für Testimonials |
| „Nur ein Scanner" | Übergabe-Modus + Dialog (I/J) als Kern-Innovation |
| WebPrüfer ähnlich | Enger Vereins-Fokus, E-Mail-Check, Wissensübergabe |
| Keine Tests im Repo | M1 explizit pytest; bewusst erste Förder-Aufgabe |
| Team-Profile fehlen (Namen noch offen) | Vier Namen + Kurzprofile bis Submit; GF/Freistellung benennen |
| Keine Antwort DsiN/BBE (Stand 04.09.) | Nachfassen bis 15.10.; parallel Landessportbund anfragen |

---

## 12. Checkliste vor Submit

- [ ] Förderschwerpunkt **Datensicherheit**
- [ ] GitHub-Link prominent
- [ ] Konkurrenz (SIWECOS, WebPrüfer, Mozilla Observatory) ehrlich benennen
- [ ] **Übergabe-Modus** als Innovation und M4-Meilenstein
- [ ] PDF **nicht** als Neuentwicklung
- [ ] Second Stage **mit beantragen**
- [ ] Privacy-by-Design explizit erwähnen
- [ ] Prüfkatalog als fachliche Tiefe referenzieren
- [ ] Text von **Nicht-Techniker** lesen lassen
- [ ] Alle 4 Namen verbindlich nennen
- [ ] Stunden vs. Meilensteine konsistent

---

## 13. Platzhalter-Status (vor dem Absenden)

### Bereits befüllt ✅

- [x] Teamgröße und Zusammensetzung: 4 IT-Ingenieur:innen, 2× Deventer
- [x] Stundenplanung: Person A Vollzeit (950 Std.), 3× je ~12 h/Woche (950 Std. gesamt)
- [x] Budget-Ziel: volle 95.000 € (+ 5 % Gemeinkosten)
- [x] GbR-Timing: erst nach Zusage (~Ende Jan. 2027), nicht vor Bewerbung
- [x] Kooperationsanfragen versendet (DsiN, BBE) — Kontakte dokumentiert
- [x] Technischer Stand: v0.3.0 mit 4 Checks, Web-UI, PDF, Formular-Check
- [x] Parallele Förderoptionen identifiziert (DSEE, NLnet)
- [x] Verworfene Alternativen dokumentiert

### Noch offen — Kristijan muss liefern ❌

- [ ] **Vollständige Namen** der vier Teammitglieder + Kurzprofile/Vorerfahrung
- [ ] **Wer ist Person A (GF)?** — Name, Wohnort DE, Freistellungsplan vom Hauptjob
- [ ] **Antworten von DsiN/BBE** — bei Zusage in Bewerbung aufnehmen; sonst Fallback-Verbände
- [ ] **DSEE-Kontakt** aufbauen (Fördermittelwerkstatt Okt./Nov. 2026)
- [ ] **Persönliche Motivation:** Kennt jemand Vereinsarbeit aus erster Hand?
- [ ] **5–10 Vereine** für Praxistests benennen (Bekanntenkreis)
- [ ] **Domain `vereinscheck.de`** — registriert? Wer hostet?
- [ ] **Frühere Förderung** für VereinsCheck oder ähnliche Idee?
- [ ] **Übergabe-Modus:** Wireframe/Mockup als Anhang
- [ ] **3–5 dokumentierte Vereins-Scans** (Screenshots + kurze Fallstudie)

### Vorhandene Entwürfe (extern, nicht im Repo)

- `VereinsCheck-Bewerbung-PrototypeFund.md` — vollständiger Bewerbungsentwurf (DE)
- `VereinsCheck-Application-English.md` — englische Version für Kolleg:innen in Deventer
- `MitWirkung-Projektplan-KA154.md` — Erasmus+-Variante (zweitrangig)

---

## 14. Zeitplan bis zur Förderung

| Phase | Zeitraum | Aktion |
|---|---|---|
| Bewerbung | 01.10.–30.11.2026 | Antrag einreichen (Förderschwerpunkt Datensicherheit) |
| Jury-Entscheidung | ca. Ende Jan. 2027 | Rückmeldung |
| Bei Zusage | Feb.–Mai 2027 | Antragsworkshop, formaler Antrag ans BMFTR, **GbR gründen** |
| Förderphase 1 | 01.06.–30.11.2027 | 6 Monate Entwicklung |
| Second Stage (optional) | Dez. 2027 – März 2028 | +4 Monate, Jury-Präsentation |

## 15. Prioritäten bis 30.11.2026

1. **Bewerbungsentwurf mit echten Namen befüllen** — Platzhalter in `VereinsCheck-Bewerbung-PrototypeFund.md` ersetzen
2. **Verbands-LOI einholen** — DsiN/BBE-Antworten nachfassen; Fallback Landessportbund
3. **Übergabe-Modus skizzieren** (Wireframe reicht) — Innovations-Beweis für Jury
4. **3–5 Vereins-Scans dokumentieren** — Screenshots + kurze Fallstudie
5. **Second Stage** planen und mit beantragen
6. **DSEE-Fördermittelwerkstatt** (Okt./Nov.) — Antragshilfe + Kontaktaufbau

---

## 16. Feature-Erweiterung — Tier-Modell (Strategie)

> **Leitplanke:** Mehr Tiefe im bestehenden Prüfkatalog — kein zweites Produkt.  
> v0.3.0 = 4 Checks · v1.0-Ziel = **7 Prüfbereiche** (A–F automatisch + I/J Dialog/Übergabe).

### Tier 1 — Must-have (6 Monate, in Meilensteinen verbindlich)

| Feature | Vereinssprache | Innovation | Aufwand | Datensicherheit |
|---|---|---|---|---|
| **E — E-Mail-Identität** (E1–E7) | „Kann jemand in eurem Namen Mails verschicken?" | CEO-Fraud-Schutz fürs Ehrenamt; DNS-only, kein Login nötig | **S** | ✅ Kern |
| **D — Formular D1–D10** | „Sind Spenden und Mitgliedsanträge sicher?" | Tracker auf Spendenseite (D8) — kein Header-Scanner liefert das | **M** | ✅ Kern |
| **F — Domain-Inventar** | „Wem gehört eure Website — und läuft sie bald ab?" | Brücke vom Scan zum Übergabe-Werkzeug | **S** | ✅ |
| **I — Geführter Dialog** | „Wer hat Zugang — und wo liegen eure Mitgliederdaten?" | Art.-30-nahes Verzeichnis ohne Anwalt; nur im Browser | **M** | ✅ Kern |
| **J — Übergabe-Modus** | „Der Vorstand wechselt — was muss der Nachfolger wissen?" | **Alleinstellungsmerkmal** — Wissen überdauert Wechsel | **M** | ✅ Kern |
| **C6/C7 — Impressum & DSE** | „Sind Pflichtseiten erreichbar?" | Schnellgewinn aus HTML; Abmahnrisiko sichtbar machen | **S** | ✅ |
| **Lösungsdatenbank** (20 Einträge) | „Was kann ich tun — Schritt für Schritt bei meinem Anbieter?" | Burggraben: Klickpfade statt generischer Tipps | **M** | ✅ |
| **pytest + Engine-Härtung** | (intern) | Glaubwürdigkeit gegenüber Jury („nur ein Hobby-Repo") | **M** | ✅ |

### Tier 2 — High-impact „Wow" (6 Monate, im Plan — Jury-Story)

| Feature | Vereinssprache | Innovation | Aufwand | Datensicherheit |
|---|---|---|---|---|
| **C1–C5 — Browser-Tracking** (Playwright) | „Wer bekommt mit, wer spendet?" | Ehrliche Prüfung statt falscher Grün-Befunde | **M/L** | ✅ |
| **A4–A7 — SSL-Tiefe** | „Ist die Verschlüsselung wirklich aktuell?" | Mixed Content, TLS-Version — ohne Panik | **S** | ✅ |
| **B — Bewertung entschärfen** | „Header fehlen — ist das schlimm?" | Gelb statt Rot bei Kleinstvereinen = Vertrauen | **S** | ✅ |
| **WCAG 2.1 AA Basics** | Barrierefrei nutzbar für alle Vorstände | Public-Interest-Standard | **M** | ○ |
| **Verbandspilot + Self-Hosting** | Multiplikator statt Einzelverein | Open Source als Verbands-Infrastruktur | **M** | ✅ |
| **Praxistests** (5–10 Vereine) | Feedback aus erster Hand | Validierung der Vereinssprache | **M** | ✅ |
| **PDF-Übergabemappe vollständig** | Eine Datei für den Nachfolger | Scan + Dialog + Checkliste in einem Export | **S** | ✅ |

### Tier 3 — Second Stage / danach (nicht im Kernversprechen)

| Feature | Warum später | Risiko wenn zu früh |
|---|---|---|
| **G — Software-Aktualität** (G1–G7) | Pfadliste konservativ; rechtlich heikel | „Angriffsscanner"-Vorwurf |
| **H — Datenspuren** (H1–H4) | Hohe Fehlerkosten, viele Grau-Befunde | Falsche Alarme, Vertrauensverlust |
| **WordPress-Plugin** | Verbreitung, nicht Kernfunktion | Scope-Explosion |
| **Domain-Verifikation** (DNS-TXT) | Wichtig für Vollprüfung, aber UX-Komplexität | Verzögert Launch |
| **E-Mail-Monitoring / Cron** | Kontinuierlicher Betrieb ≠ Prototyp | SaaS-Narrativ, Wartungslast |
| **Wiedervorlage-Erinnerungen** | Nice-to-have nach etabliertem Tool | Push ohne Nutzerbasis |

### Scope-Fallen — explizit NICHT versprechen

- Penetration Testing, Fuzzing, Brute-Force (Prüfkatalog verbietet das)
- Testdaten in fremde Formulare senden
- Nutzerkonten, Scan-Historie, Cloud-Speicherung (bricht Privacy-by-Design)
- KI-Chatbot, automatische Rechtsberatung
- Mobile App, Mehrsprachigkeit, Enterprise-Dashboard
- Vollautomatisches Art.-30-Dokument (nur „nahe Übersicht" aus Dialog)

### 5 Features, die „mehr" fühlen lassen — ohne Produktwechsel

1. **E-Mail-Identität** — neuer roter Befund, den jeder Schatzmeister versteht  
2. **Formular D8** (Tracker auf Spendenseite) — schockiert Vorstände sofort  
3. **Domain-Inventar + Ablaufdatum** — Existenzrisiko, nicht nur Technik  
4. **Übergabe-Modus** — einziger Check, der den Vorstandswechsel adressiert  
5. **Lösungsdatenbank** — „klick hier bei IONOS" statt generischem Rat  

### Innovation in einem Satz (Pitch)

> **VereinsCheck ist der erste Sicherheits-Check für Vereine, der Website-Prüfung (von HTTPS über Spendenformulare bis E-Mail-Schutz) mit einer übergabefähigen Datenschutz-Mappe für den Vorstandswechsel verbindet — ohne Vereinsdaten zu speichern.**

### Optionaler Quick-Win vor Bewerbung (Code)

| Maßnahme | Aufwand | Nutzen |
|---|---|---|
| `checks/email_check.py` Stub (SPF/DMARC per DNS) | ~2 h | 5. Check live → Pitch glaubwürdiger |
| Wireframe Übergabe-Modus (3 Screens) | Person D | Innovations-Beweis ohne Implementierung |
| 1 Fallstudie mit rotem E-Mail-Befund | ~30 min | Story für Feld „Gesellschaftliche Herausforderung" |

→ E-Mail-Stub **nicht zwingend** — Prüfkatalog + Meilensteine reichen; Stub nur wenn vor Submit noch Kapazität.
