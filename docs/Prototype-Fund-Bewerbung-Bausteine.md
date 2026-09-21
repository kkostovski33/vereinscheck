# VereinsCheck – Bewerbungsbausteine Prototype Fund

*Aktualisierter Stand: 21.09.2026 – inkl. Prüfkatalog, korrigierter Roadmap und fertiger Antworttexte*

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
machen, den Prüfkatalog (10 Bereiche, siehe Projektdokumentation) umsetzen und 
über Dachverbände in die Breite tragen.
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

Geplante Erweiterungen in der Förderphase (Priorität laut Prüfkatalog):
- E: E-Mail-Identität (SPF/DMARC/DKIM) – hoher Erkenntniswert, DNS-only
- D: Formular-Check auf D1–D10 ausbauen (Kern-Differenzierung)
- F + I + J: Domain-Inventar, Zugangsregister-Dialog, Übergabe-Modus
- C: Browser-basierte Tracking-Prüfung (Playwright), sonst grau statt grün
- pytest-Testabdeckung, barrierefreies Frontend, EU-Hosting

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

Monat 1–2 – Engine härten:
Unit-/Integrationstests (pytest) für alle vier Checks. Scan-Logik anhand 
mindestens 50 realer Vereins-Websites verfeinern. Fehlertoleranz bei 
nicht erreichbaren Seiten, Redirects, gemischten HTTP/HTTPS-Setups.

Monat 2–3 – Checks erweitern (Prüfkatalog E + D):
Neues Modul E-Mail-Identität (SPF, DMARC, DKIM via DNS). Formular-Check 
auf D1–D10 ausbauen (GET statt POST, Tracker auf Spendenseite, Zahlungsdienst-
Einordnung). PDF plattformunabhängig machen (Font-Handling für Linux-Server).

Monat 3–4 – Übergabe-Werkzeug (Prüfkatalog F, I, J – Alleinstellungsmerkmal):
Domain-/Hosting-Inventar (WHOIS, Registrar, Ablaufdatum). Geführter Dialog 
(10–15 Fragen in Vereinssprache) → Zugriffsregister. Übergabe-Modus mit 
PDF-Export und Entzugs-Checkliste beim Vorstandswechsel. Usability-Test 
mit 3 Vereinsvorständen.

Monat 4–5 – Frontend & Barrierefreiheit:
Web-Oberfläche optimieren (Mobile, WCAG 2.1 AA Basics). Praxistests mit 
5–10 Vereinen, Feedback einarbeiten. Lösungsdatenbank: 20 Starteinträge 
(WordPress, IONOS, Strato, Twingle …).

Monat 5–6 – Verbreitung & Nachhaltigkeit:
Pilot mit mindestens einem Dachverband. Self-Hosting-Doku für Verbände. 
Öffentliches Hosting unter eigener Domain. Veröffentlichung v1.0.

Meilensteine: M2 = getestete Engine; M3 = E-Mail- + Formular-Checks; 
M4 = Übergabe-Modus; M5 = Praxistests abgeschlossen; M6 = v1.0 live.
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
- Kooperationsanfragen bereits versendet; Ziel: schriftliche 
  Interessensbestätigung für Testphase mit Mitgliedsvereinen
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

**Geplant in der Förderphase (klar abgrenzbar):**
1. Testabdeckung und Robustheit der Engine
2. Prüfkatalog-Bereiche E, D (voll), F, I, J (noch nicht im Code)
3. Browser-basierte Tracking-Prüfung (C5–C7)
4. Barrierefreies Frontend + Praxistests mit echten Vereinen
5. Lösungsdatenbank (anbieterspezifische Klickpfade)
6. Verbands-Pilot und öffentliches Hosting

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

## 10. Team & Formalien

- Max. **4 Personen**, nach Auswahl **GbR mit Sitz in Deutschland**
- Geschäftsführer:in mit Wohnsitz in DE (Teammitglieder in NL/Deventer: OK)
- Open Source (MIT ✅)
- **Kein** Verein, Unternehmen oder Uni als Antragsteller

| Person | Rolle (Vorschlag) | Arbeitspaket |
|---|---|---|
| Person A (DE, GF) | Projektleitung, Verbands-Kontakte | M5–M6, GbR |
| Person B | Scan-Engine, Tests | M1–M3 |
| Person C | Frontend, Barrierefreiheit | M4–M5 |
| Person D | Übergabe-Modus, UX-Texte, Prüfkatalog | M3–M4 |

**Stunden (Richtwert):** ca. 3.800–4.200 Stunden gesamt (4 × ~20–25 h/Woche × 26 Wochen)

---

## 11. Schwächen & Gegenmaßnahmen

| Schwäche | Gegenmaßnahme |
|---|---|
| Keine LOI von Verbänden | Bis 30.11. Antworten einholen; 2–3 Vereine für Testimonials |
| „Nur ein Scanner" | Übergabe-Modus + Dialog (I/J) als Kern-Innovation |
| WebPrüfer ähnlich | Enger Vereins-Fokus, E-Mail-Check, Wissensübergabe |
| Keine Tests im Repo | M1 explizit pytest; bewusst erste Förder-Aufgabe |
| Team-Profile fehlen | Namen, GitHub-Links, Motivation ergänzen |

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

## 13. Noch auszufüllende Platzhalter (vor dem Absenden)

- [ ] Vollständige Namen der vier Teammitglieder + Kurzprofile/Vorerfahrung
- [ ] Konkrete GbR-Konstellation (wer Geschäftsführung, Sitz in Deutschland)
- [ ] Antworten von DsiN/BBE/DSEE — bei Zusage in Bewerbung aufnehmen
- [ ] Persönliche Motivation: Kennt jemand Vereinsarbeit aus erster Hand?
- [ ] Stundenplanung: Vollzeit-Freistellung oder Nebenprojekt?
- [ ] 5–10 Vereine für Praxistests (Bekanntenkreis)?
- [ ] Domain `vereinscheck.de` — registriert? Wer hostet?
- [ ] Frühere Förderung für VereinsCheck oder ähnliche Idee?
- [ ] Übergabe-Modus: Wireframe/Mockup als Anhang?

---

## 14. Prioritäten bis 30.11.2026

1. **Übergabe-Modus skizzieren** (Wireframe reicht) — Innovations-Beweis
2. **Verbands-LOI einholen** — auch informelle E-Mail von DsiN/BBE ist Gold wert
3. **3–5 Vereins-Scans dokumentieren** — Screenshots + Fallstudie
4. **Team-Profile + GbR-Konstellation** ausfüllen
5. **Second Stage** planen und mit beantragen
