# VereinsCheck

**Verständlicher IT-Sicherheits-Check für Vereine – Open Source, ohne Fachchinesisch.**

VereinsCheck prüft die Website eines Vereins in unter 2 Minuten auf grundlegende
IT-Sicherheit und gibt eine verständliche **Ampel-Bewertung** statt Fachjargon aus.

Hintergrund: Rund 600.000 Vereine in Deutschland werden ehrenamtlich geführt,
Vorstände wechseln oft alle 1–2 Jahre. Mit jedem Wechsel geht IT-Wissen verloren.
VereinsCheck soll diese Lücke schließen.

## Was wird geprüft?

| Check | Was er bedeutet |
|---|---|
| **HTTPS-Verschlüsselung** | Ist die Seite über HTTPS erreichbar und das Zertifikat gültig / nicht bald abgelaufen? |
| **Security-Header** | Setzt die Seite wichtige Schutz-Header (HSTS, CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy)? |
| **Tracking & Cookies** | Werden bekannte Tracker geladen, und gibt es ein Cookie-/Consent-Tool? |

Die Ausgabe erfolgt als Ampel: **grün** (alles gut), **gelb** (Verbesserungspotenzial),
**rot** (dringender Handlungsbedarf).

## Installation

```bash
git clone https://github.com/kkostovski33/vereinscheck.git
cd vereinscheck
pip install -r requirements.txt
```

## Nutzung

```bash
python scanner.py https://www.mein-verein.de
```

Beispiel-Ausgabe:

```
============================================================
  VereinsCheck – Sicherheits-Check fuer: www.mein-verein.de
============================================================

[ GRUEN ]  HTTPS-Verschluesselung
          HTTPS ist aktiv und das Zertifikat ist noch 57 Tage gueltig.

[ ROT   ]  Security-Header
          Nur 1 von 5 Security-Headern gesetzt. Es fehlen: ...
```

## Projektstruktur

```
vereinscheck/
├── scanner.py           # Startpunkt: lädt die Seite und gibt die Ampel aus
├── checks/              # Ein Modul pro Prüfung (im Team parallel erweiterbar)
│   ├── ssl_check.py     # HTTPS / Zertifikat
│   ├── headers_check.py # Security-Header
│   └── tracking_check.py# Tracking & Cookies
├── requirements.txt
└── README.md
```

## Roadmap

- [ ] **Formular-Check** für Spenden-/Mitgliedsformulare (nächster Schritt)
- [ ] Klartext-Report im Ampel-Format zum Weitergeben
- [ ] Übergabe-Checkliste für den nächsten Vorstand
- [ ] Minimalistisches Web-Frontend

## Lizenz

Open Source. Lizenz folgt (geplant: MIT).

---

*VereinsCheck ist ein gemeinnütziges Open-Source-Projekt.*
