# VereinsCheck

**Kostenloser IT-Sicherheits-Check für deutsche Vereine — verständlich, ohne Fachchinesisch.**

VereinsCheck prüft die Website eines Vereins in unter 2 Minuten auf grundlegende IT-Sicherheit und Datenschutz. Die Ergebnisse werden als Ampel-Bewertung mit konkreten Handlungsempfehlungen auf Deutsch ausgegeben — auch ohne IT-Kenntnisse verständlich.

Ein automatisch generierter **PDF-Bericht** kann direkt an den Webmaster weitergeleitet werden.

---

## Was wird geprüft?

| Check | Was er bedeutet |
|---|---|
| **HTTPS & Zertifikat** | Ist die Verbindung verschlüsselt? Ist das Zertifikat gültig und noch nicht abgelaufen? |
| **Security-Header** | Sind die 5 wichtigsten Server-Schutzeinstellungen aktiv? (HSTS, CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy) |
| **Tracking & DSGVO** | Werden Besucher von Google, Meta oder anderen ohne Einwilligung getrackt? |
| **Formular-Sicherheit** | Werden Mitgliedsdaten und IBANs verschlüsselt übertragen? |

---

## Warum VereinsCheck?

Über 600.000 Vereine in Deutschland verwalten sensible Mitgliederdaten — aber kaum einer hat Budget für IT-Sicherheitsberatung. Bestehende Tools wie Mozilla Observatory oder SSL Labs sind für Entwickler gemacht: technische Rohdaten, kein Kontext, kein Handlungsplan.

VereinsCheck schließt diese Lücke: **kein Englisch, kein Fachjargon, keine IT-Kenntnisse nötig.**

---

## Datenschutz

VereinsCheck speichert **keine** eingegebenen URLs, keine Scan-Ergebnisse, keine IP-Adressen, keine Cookies. Jede Anfrage wird vollständig im Arbeitsspeicher verarbeitet und danach verworfen. Es gibt keine Datenbank.

→ [Datenschutzerklärung](https://vereinscheck.de/datenschutz) *(nach Launch verfügbar)*

---

## Installation & lokale Nutzung

```bash
git clone https://github.com/kkostovski33/vereinscheck.git
cd vereinscheck
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Dann im Browser öffnen: [http://localhost:8080](http://localhost:8080)

### Voraussetzungen

- Python 3.10+
- macOS: Arial Unicode.ttf ist unter `/System/Library/Fonts/Supplemental/` vorhanden (für PDF-Export)

---

## Projektstruktur

```
vereinscheck/
├── app.py               # Flask-App, Routen
├── bericht.py           # PDF-Generator (fpdf2)
├── checks/
│   ├── ssl_check.py     # HTTPS & Zertifikat
│   ├── headers_check.py # Security-Header
│   ├── tracking_check.py# Tracking & DSGVO
│   └── form_check.py    # Formular-Sicherheit
├── templates/
│   ├── index.html       # Haupt-Interface
│   └── datenschutz.html # Datenschutzerklärung
├── requirements.txt
└── VERSION              # Semantische Versionierung
```

---

## Roadmap

- [x] SSL/TLS-Check
- [x] Security-Header-Check
- [x] Tracking & DSGVO-Check
- [x] Formular-Sicherheits-Check
- [x] PDF-Bericht (weiterleitbar an Webmaster)
- [x] Datenschutzerklärung
- [ ] DMARC & DNSSEC-Check
- [ ] Datenschutzerklärung-Erkennung auf Zielseite
- [ ] Öffentliches Hosting unter eigener Domain
- [ ] Automatisches E-Mail-Monitoring für Vereine
- [ ] WordPress-Plugin

---

## Lizenz

MIT — siehe [LICENSE](LICENSE)
