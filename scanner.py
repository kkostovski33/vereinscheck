#!/usr/bin/env python3
"""VereinsCheck – kostenloser IT-Sicherheits-Check fuer Vereins-Websites.

Aufruf:
    python scanner.py https://www.mein-verein.de

Prueft in unter 2 Minuten:
  1. HTTPS-Verschluesselung (SSL/TLS-Zertifikat)
  2. Security-Header
  3. Tracking & Cookies (heuristisch)

Ausgabe als verstaendliche Ampel – ohne Fachchinesisch.
"""

import sys
from urllib.parse import urlparse

import requests

from checks.ssl_check import check_ssl
from checks.headers_check import check_headers
from checks.tracking_check import check_tracking

AMPEL_SYMBOL = {"gruen": "[ GRUEN ]", "gelb": "[ GELB  ]", "rot": "[ ROT   ]"}


def normalisiere_url(eingabe: str) -> str:
    """Ergaenzt fehlendes https:// und entfernt Leerzeichen."""
    eingabe = eingabe.strip()
    if not eingabe.startswith(("http://", "https://")):
        eingabe = "https://" + eingabe
    return eingabe


def hole_seite(url: str):
    """Laedt die Seite und gibt das Response-Objekt zurueck (oder None bei Fehler)."""
    try:
        return requests.get(
            url,
            timeout=15,
            headers={"User-Agent": "VereinsCheck/0.1 (+https://github.com/kkostovski33/vereinscheck)"},
            allow_redirects=True,
        )
    except requests.RequestException as exc:
        print(f"\nFehler: Die Seite {url} konnte nicht geladen werden ({exc}).")
        return None


def drucke_ergebnis(ergebnis: dict) -> None:
    symbol = AMPEL_SYMBOL.get(ergebnis["ampel"], "[ ????  ]")
    print(f"{symbol}  {ergebnis['titel']}")
    print(f"          {ergebnis['details']}\n")


def main() -> int:
    if len(sys.argv) < 2:
        print("Bitte eine Website angeben, z. B.:")
        print("    python scanner.py https://www.mein-verein.de")
        return 1

    url = normalisiere_url(sys.argv[1])
    hostname = urlparse(url).hostname
    if not hostname:
        print("Das sieht nicht wie eine gueltige Website-Adresse aus.")
        return 1

    print("\n" + "=" * 60)
    print(f"  VereinsCheck – Sicherheits-Check fuer: {hostname}")
    print("=" * 60 + "\n")

    ergebnisse = []

    # 1. HTTPS / SSL – funktioniert unabhaengig vom Laden der Seite
    ergebnisse.append(check_ssl(hostname))

    # 2. + 3. brauchen den Seiteninhalt
    antwort = hole_seite(url)
    if antwort is not None:
        ergebnisse.append(check_headers(antwort))
        ergebnisse.append(check_tracking(antwort.text))
    else:
        ergebnisse.append({
            "ampel": "gelb", "titel": "Security-Header",
            "details": "Konnte nicht geprueft werden, weil die Seite nicht geladen werden konnte.",
        })
        ergebnisse.append({
            "ampel": "gelb", "titel": "Tracking & Cookies",
            "details": "Konnte nicht geprueft werden, weil die Seite nicht geladen werden konnte.",
        })

    for ergebnis in ergebnisse:
        drucke_ergebnis(ergebnis)

    # Kurzes Gesamt-Fazit
    if any(e["ampel"] == "rot" for e in ergebnisse):
        print("Fazit: Es gibt dringenden Handlungsbedarf (rote Punkte oben).")
    elif any(e["ampel"] == "gelb" for e in ergebnisse):
        print("Fazit: Grundsaetzlich ok, aber es gibt Verbesserungspunkte (gelb).")
    else:
        print("Fazit: Sehr gut – alle Basis-Checks sind gruen!")
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
