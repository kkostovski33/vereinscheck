"""Security-Header-Check: Setzt die Website die wichtigsten Schutz-Header?"""

WICHTIGE_HEADER = {
    "strict-transport-security": "HSTS (erzwingt HTTPS im Browser)",
    "content-security-policy": "CSP (Schutz vor eingeschleustem Code)",
    "x-frame-options": "X-Frame-Options (Schutz vor Clickjacking)",
    "x-content-type-options": "X-Content-Type-Options (verhindert MIME-Tricks)",
    "referrer-policy": "Referrer-Policy (weniger Datenabfluss beim Weiterklicken)",
}


def check_headers(response) -> dict:
    """Erwartet ein requests.Response-Objekt und prueft die Security-Header.

    Rueckgabe: dict mit 'ampel', 'titel' und 'details'.
    """
    # Header case-insensitive einlesen
    vorhandene = {k.lower() for k in response.headers.keys()}

    gefunden = []
    fehlend = []
    for header, beschreibung in WICHTIGE_HEADER.items():
        if header in vorhandene:
            gefunden.append(beschreibung)
        else:
            fehlend.append(beschreibung)

    anzahl = len(gefunden)

    if anzahl == len(WICHTIGE_HEADER):
        ampel = "gruen"
        text = "Alle fuenf wichtigen Security-Header sind gesetzt."
    elif anzahl >= 3:
        ampel = "gelb"
        text = f"{anzahl} von 5 Security-Headern gesetzt. Es fehlen noch: " + ", ".join(fehlend) + "."
    else:
        ampel = "rot"
        text = f"Nur {anzahl} von 5 Security-Headern gesetzt. Es fehlen: " + ", ".join(fehlend) + "."

    return {"ampel": ampel, "titel": "Security-Header", "details": text}
