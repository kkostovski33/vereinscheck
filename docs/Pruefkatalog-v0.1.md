# VereinsCheck – Prüfkatalog

**Version 0.1 (Entwurf) · Stand: September 2026**

Dieses Dokument ist die fachliche Spezifikation von VereinsCheck. Es beschreibt, was geprüft wird, warum es für einen Verein zählt, wie das Ergebnis bewertet wird und welche konkrete Handlung daraus folgt.

**Drei Zwecke:**
1. Produktspezifikation für die Entwicklung (`checks/`)
2. Grundlage für verständliche Texte im PDF-Bericht
3. Nachweis der inhaltlichen Tiefe gegenüber Förderern und Partnern

---

## Leitprinzipien

- **Vereinssprache vor Fachsprache.** Jeder Befund hat einen Namen, den ein Schatzmeister versteht. Der technische Begriff steht in Klammern dahinter, nicht davor.
- **Kein Befund ohne Handlung.** Zu jedem roten oder gelben Befund gehört ein Klickpfad beim Anbieter — oder ein Textbaustein für die Mail an den Webmaster.
- **Nur passive Prüfungen.** Keine Angriffssimulation, keine Testdaten in fremde Formulare, kein Bruteforce.
- **Befunde altern.** Jeder Bericht trägt ein Prüfdatum und einen Hinweis zur nächsten Prüfung.

---

## Bewertungslogik

| Ampel | Bedeutung | Konsequenz im Bericht |
|---|---|---|
| **Rot** | Risiko für Mitgliederdaten/Vereinsgeld oder Rechtsverstoß | Ganz oben, mit Frist-Empfehlung |
| **Gelb** | Sollte behoben werden, kein akutes Risiko | Mittlerer Block |
| **Grün** | In Ordnung | Kurzbestätigung |
| **Grau** | Nicht prüfbar | Als „nicht geprüft" — **nie** still zu Grün |

**Gesamtampel:** Ein roter Befund in **D (Formulare)** oder **E (E-Mail-Identität)** färbt die Gesamtampel rot — kein Durchschnitt.

---

## A. Erreichbarkeit und Verschlüsselung

*Vereinssprache: „Ist die Verbindung zu eurer Website sicher?"*

| ID | Prüfung | Rot | Gelb |
|---|---|---|---|
| A1 | HTTPS verfügbar | nur HTTP | — |
| A2 | Weiterleitung HTTP→HTTPS | keine | nur Startseite |
| A3 | Zertifikat gültig | abgelaufen/falsch/selbstsigniert | läuft in <14 Tagen ab |
| A4 | Zertifikatskette | unvollständig | — |
| A5 | TLS-Version | TLS 1.0/1.1 aktiv | TLS 1.2 ohne 1.3 |
| A6 | Unsichere Cipher | gebrochene Verfahren | veraltete |
| A7 | Mixed Content | HTTP-Ressourcen auf HTTPS-Seite | — |

**Stand v0.3.0:** Grundlage vorhanden · **Nächste Stufe:** A4–A7

---

## B. Server-Schutzeinstellungen (Security-Header)

*Vereinssprache: „Schützt euer Server die Besucher vor typischen Tricks?"*

| ID | Header | Bewertung |
|---|---|---|
| B1 | HSTS | fehlt = gelb; max-age <6 Monate = gelb |
| B2 | CSP | fehlt = gelb; unsafe-inline = gelb mit Hinweis |
| B3 | X-Frame-Options | fehlt = gelb |
| B4 | X-Content-Type-Options | fehlt = gelb |
| B5 | Referrer-Policy | fehlt = gelb; unsafe-url auf Formularseite = **rot** |
| B6 | Permissions-Policy | fehlt = grau |
| B7 | Server-Version sichtbar | gelb |

**Stand v0.3.0:** vorhanden · **Nächste Stufe:** Bewertung entschärfen, B6/B7

---

## C. Tracking, Drittanbieter und Einwilligung

*Vereinssprache: „Wer bekommt mit, wer eure Seite besucht?"*

| ID | Prüfung | Rot wenn |
|---|---|---|
| C1 | Tracking vor Einwilligung | GA, Meta Pixel o.ä. ohne Zustimmung |
| C2 | Google Fonts/Maps extern | IP-Übertragung ohne Einwilligung |
| C3 | YouTube-Einbettung | ohne youtube-nocookie + ohne Einwilligung |
| C4 | Cookies vor Einwilligung | Tracking-Cookies ohne Zustimmung |
| C5 | Einwilligungsbanner | Ablehnen nicht gleichwertig möglich |
| C6 | Datenschutzerklärung | nicht auffindbar = rot; ohne Dienste = gelb |
| C7 | Impressum | nicht auffindbar = rot (§ 5 DDG) |

**Methodik:** C1–C4 brauchen Browser-Lauf (Playwright) — sonst **grau**, nicht grün.

**Stand v0.3.0:** heuristisch · **Nächste Stufe:** Browser-Prüfung, C5–C7

---

## D. Formular- und Zahlungssicherheit — Kernbereich

*Vereinssprache: „Sind Mitgliedsanträge und Spenden sicher?"*

| ID | Prüfung | Rot wenn |
|---|---|---|
| D1 | Formular-Ziel verschlüsselt | action → http:// |
| D2 | Ziel auf Fremddomain | Daten an andere Domain |
| D3 | Sensible Felder | IBAN/Geburtsdatum auf unverschlüsselter Seite |
| D4 | Übertragungsmethode | GET statt POST |
| D5 | Autocomplete Bankdaten | autocomplete nicht deaktiviert bei IBAN |
| D6 | CSRF-Schutz | kein Token-Feld |
| D7 | Zahlungsdienstleister | PayPal, Mollie, Twingle … — Einordnung |
| D8 | Tracker auf Formularseite | Meta-Pixel auf Spendenseite (**Art. 9 DSGVO**) |
| D9 | Bestätigungsseite | personenbezogene Daten in URL |
| D10 | Datei-Upload | ohne Typbeschränkung |

**Rechtliche Grenze:** Nur HTML-Analyse — nie Testdaten senden.

**Stand v0.3.0:** Grundlage · **Nächste Stufe:** D1–D10 voll — **Priorität**

---

## E. E-Mail-Identität — neu

*Vereinssprache: „Kann jemand in eurem Namen Mails verschicken?"*

| ID | Prüfung | Rot/Gelb |
|---|---|---|
| E1 | SPF-Eintrag | fehlt = rot |
| E2 | SPF-Policy | +all = rot |
| E3 | DMARC-Eintrag | fehlt = rot |
| E4 | DMARC-Policy | p=none = gelb |
| E5 | DKIM | kein Selector = gelb |
| E6 | MX-Einträge | Anbieter benennen |
| E7 | Mailanbieter | Freemail als Vereinsadresse = gelb |

**Stand v0.3.0:** offen · **Nächste Stufe:** DNS-only — **Priorität, hoher Wert**

---

## F. Domain- und Hosting-Inventar — neu

*Vereinssprache: „Wem gehört eigentlich eure Website?"*

| ID | Prüfung | Befund |
|---|---|---|
| F1 | Domain-Ablaufdatum | <60 Tage = rot, <6 Monate = gelb |
| F2 | Registrar | benennen |
| F3 | Hosting-Anbieter | aus IP/ASN |
| F4 | Serverstandort | Land (Drittlandtransfer-Hinweis) |
| F5 | Nameserver | benennen |
| F6 | DNSSEC | nicht aktiv = grau |

**Stand v0.3.0:** offen · **Nächste Stufe:** WHOIS/DNS — Übergabe-Story

---

## G. Software-Aktualität — Second Stage

| ID | Prüfung | Rot wenn |
|---|---|---|
| G1 | CMS-Version | veraltete Hauptversion |
| G2 | Verzeichnislisting | öffentlich auflistbar |
| G3 | /.git/ erreichbar | Quellcode öffentlich |
| G4 | Backup-Dateien | .sql, .zip an typischen Pfaden |
| G5 | /.env erreichbar | Konfigdateien öffentlich |
| G6 | Admin-Login | /wp-admin exponiert = gelb |
| G7 | wp-json/users | Benutzernamen abrufbar = gelb |

**Methodik:** Feste Pfadliste — kein Fuzzing.

---

## H. Datenspuren im Netz — Second Stage

| ID | Prüfung | Befund |
|---|---|---|
| H1 | PDFs mit Personendaten | Mitgliederlisten öffentlich verlinkt |
| H2 | Private Kontaktdaten | über Impressum hinaus |
| H3 | Fotos mit Kindern | nur Hinweis, kein automatisches Urteil |
| H4 | robots.txt/Sitemap | verweist auf interne Bereiche |

---

## I. Geführter Dialog — Innovationskern

10–15 Fragen in Vereinssprache → Zugriffs- und Verantwortlichkeitsregister (Art.-30-nah).

1. Wer hat Zugang zum Website-Verwaltungsbereich?
2. Wer hatte früher Zugang und hat ihn noch?
3. Auf wen läuft Domain/Hosting-Vertrag? Wer zahlt?
4. Wo liegt die Mitgliederliste?
5. Wer hat Zugriff auf Vereinspostfach?
6. Wer hat Zugriff auf Vereinskonto/Spendentool?
7. Werden Mitgliederdaten über WhatsApp/private Mail geteilt?
8. Gibt es Backups? Wer prüft sie?
9. Welche Dienstleister verarbeiten Daten?
10. Was passiert beim nächsten Vorstandswechsel?

**Datenschutz:** Verarbeitung nur im Browser, PDF-Ausgabe, keine Serverspeicherung.

**Stand v0.3.0:** offen · **Förderphase M3–M4**

---

## J. Übergabe-Modus — Innovationskern

Modus „Der Vorstand wechselt":
- Entzugs-Checkliste pro Dienst
- Vertragsüberschreibung (Domain, Hosting, Software)
- **Übergabemappe PDF:** Inventar (F) + Register (I) + offene Befunde + Unterschriften
- Wiedervorlage nach 12 Monaten

**Stand v0.3.0:** offen · **Förderphase M4** · Spec: [`Übergabe-Modus-Spezifikation.md`](./Übergabe-Modus-Spezifikation.md)

---

## Lösungsdatenbank

Anbieterspezifische Klickpfade für: WordPress, IONOS, Strato, Jimdo, Wix, Twingle, betterplace, PayPal, Mollie …

**Stand v0.3.0:** Ansätze · **Förderphase:** 20 Starteinträge

---

## Rechtliche Leitplanken

1. Domain-Verifizierung vor Vollprüfung (DNS-TXT oder Datei im Web-Root)
2. Nur passive Prüfungen
3. Rate-Limiting pro Domain und IP
4. Klarer User-Agent mit Info-Seite
5. Opt-out für Domaininhaber
6. Keine Ergebnis-Speicherung ohne Zustimmung
7. Disclaimer: kein Sicherheitsaudit, kein Rechtsrat — Grün = „in geprüften Punkten unauffällig"

---

## Priorisierung Förderphase

| Priorität | Bereiche | Begründung |
|---|---|---|
| **1** | E, D | Schnell + hoher Vereins-Nutzen |
| **2** | F, I, J | Übergabe-Werkzeug-Story |
| **3** | C (Browser), A4–A7, B | Qualität bestehender Checks |
| **Second Stage** | G, H | Vorsichtig, höhere Fehlerkosten |
