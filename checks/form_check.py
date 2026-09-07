"""Formular-Check: Sind Spenden-/Mitgliedsformulare sicher gebaut?

Formulare sind der Ort, wo Vereine die sensibelsten Daten sammeln
(Name, Adresse, IBAN, Geburtsdatum). Dieser Check sucht solche Formulare
und prueft, ob sie datensparsam und sicher uebertragen werden.
"""

from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

# Schluesselwoerter, die auf sensible Eingabefelder hindeuten
SENSIBLE_FELDER = {
    "E-Mail": ["email", "e-mail", "mail"],
    "Name": ["name", "vorname", "nachname", "firstname", "lastname"],
    "Adresse": ["adresse", "address", "strasse", "straße", "street", "plz", "ort", "city", "postal"],
    "IBAN/Bank": ["iban", "konto", "bank", "bic"],
    "Geburtsdatum": ["geburt", "birth", "dob"],
    "Telefon": ["telefon", "phone", "tel", "mobil"],
}


def _feld_text(feld) -> str:
    """Sammelt alle Attribute eines Eingabefeldes zu einem durchsuchbaren Text."""
    teile = [
        feld.get("name", ""), feld.get("id", ""), feld.get("type", ""),
        feld.get("placeholder", ""), feld.get("autocomplete", ""),
    ]
    return " ".join(teile).lower()


def _sensible_felder_im_formular(formular) -> list:
    """Gibt die Liste der gefundenen sensiblen Feld-Kategorien zurueck."""
    gefunden = set()
    for feld in formular.find_all(["input", "textarea", "select"]):
        text = _feld_text(feld)
        for kategorie, schluessel in SENSIBLE_FELDER.items():
            if any(s in text for s in schluessel):
                gefunden.add(kategorie)
    return sorted(gefunden)


def check_forms(html: str, base_url: str) -> dict:
    """Prueft alle Formulare einer Seite auf sichere Datenuebertragung.

    Rueckgabe: dict mit 'ampel', 'titel' und 'details'.
    """
    soup = BeautifulSoup(html, "html.parser")
    formulare = soup.find_all("form")

    if not formulare:
        return {
            "ampel": "gruen", "titel": "Formular-Sicherheit",
            "details": "Auf dieser Seite wurde kein Formular gefunden.",
        }

    # Gibt es irgendwo auf der Seite einen Datenschutz-Hinweis/Link?
    seite_hat_datenschutz = "datenschutz" in html.lower() or "privacy" in html.lower()

    probleme = []   # rote Befunde
    hinweise = []   # gelbe Befunde
    sensible_gefunden = False

    for i, formular in enumerate(formulare, start=1):
        felder = _sensible_felder_im_formular(formular)
        if not felder:
            continue  # unkritisches Formular (z. B. reine Suche) -> ueberspringen
        sensible_gefunden = True

        # 1. Uebertragungsweg: HTTPS? GET oder POST?
        methode = (formular.get("method") or "get").lower()
        aktion = formular.get("action") or base_url
        ziel = urljoin(base_url, aktion)
        ziel_schema = urlparse(ziel).scheme

        if ziel_schema and ziel_schema != "https":
            probleme.append(f"Formular {i} ({', '.join(felder)}) sendet Daten UNVERSCHLUESSELT (kein HTTPS).")
        if methode == "get":
            probleme.append(f"Formular {i} ({', '.join(felder)}) nutzt die Methode GET – sensible Daten landen sichtbar in der Adresszeile.")

        # 2. Datenschutz-Einwilligung in der Naehe?
        formular_html = str(formular).lower()
        hat_checkbox = bool(formular.find("input", {"type": "checkbox"}))
        hat_datenschutz_bezug = ("datenschutz" in formular_html or "einwillig" in formular_html
                                 or hat_checkbox)
        if not hat_datenschutz_bezug and not seite_hat_datenschutz:
            hinweise.append(f"Formular {i}: keine erkennbare Datenschutz-Einwilligung oder -Verlinkung in der Naehe.")

        # 3. Drittanbieter (eingebettetes iframe, z. B. Zahlungsdienstleister)
        if formular.find("iframe"):
            hinweise.append(f"Formular {i}: enthaelt ein eingebettetes Fremd-Element (iframe) – bitte pruefen, wohin die Daten gehen.")

        # 4. (Nice-to-have) Autocomplete bei IBAN-Feldern deaktiviert?
        if "IBAN/Bank" in felder:
            for feld in formular.find_all("input"):
                text = _feld_text(feld)
                if "iban" in text and "off" not in (feld.get("autocomplete") or ""):
                    hinweise.append(f"Formular {i}: beim IBAN-Feld ist 'autocomplete' nicht deaktiviert.")
                    break

    if not sensible_gefunden:
        return {
            "ampel": "gruen", "titel": "Formular-Sicherheit",
            "details": "Formulare gefunden, aber keine mit sensiblen Feldern (z. B. Name, IBAN).",
        }

    if probleme:
        text = "Kritisch: " + " ".join(probleme)
        if hinweise:
            text += " Ausserdem: " + " ".join(hinweise)
        return {"ampel": "rot", "titel": "Formular-Sicherheit", "details": text}

    if hinweise:
        return {"ampel": "gelb", "titel": "Formular-Sicherheit",
                "details": "Verbesserungspunkte: " + " ".join(hinweise)}

    return {"ampel": "gruen", "titel": "Formular-Sicherheit",
            "details": "Sensible Formulare gefunden – Uebertragung verschluesselt (HTTPS/POST) und Datenschutz-Bezug vorhanden."}
