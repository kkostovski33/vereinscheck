"""Tracking-/Cookie-Check (heuristisch): Werden bekannte Tracker geladen und gibt es ein Consent-Tool?"""

import re

# Bekannte Tracker / Analyse-Dienste (Ausschnitt, leicht erweiterbar)
BEKANNTE_TRACKER = {
    "google-analytics.com": "Google Analytics",
    "googletagmanager.com": "Google Tag Manager",
    "google.com/recaptcha": "Google reCAPTCHA",
    "connect.facebook.net": "Facebook Pixel",
    "facebook.com/tr": "Facebook Pixel",
    "hotjar.com": "Hotjar",
    "doubleclick.net": "Google DoubleClick",
    "matomo": "Matomo",
    "youtube.com/embed": "YouTube-Einbettung",
    "fonts.googleapis.com": "Google Fonts (extern geladen)",
}

# Hinweise auf ein Cookie-/Consent-Tool
CONSENT_HINWEISE = [
    "cookiebot", "usercentrics", "borlabs", "complianz", "cookieconsent",
    "klaro", "consentmanager", "onetrust", "cookie-consent", "cookiefirst",
]


def check_tracking(html: str) -> dict:
    """Durchsucht den HTML-Quelltext heuristisch nach Trackern und Consent-Tools.

    Rueckgabe: dict mit 'ampel', 'titel' und 'details'.
    """
    text = html.lower()

    gefundene_tracker = sorted({
        name for muster, name in BEKANNTE_TRACKER.items() if muster in text
    })
    hat_consent = any(hinweis in text for hinweis in CONSENT_HINWEISE)

    if not gefundene_tracker:
        return {
            "ampel": "gruen",
            "titel": "Tracking & Cookies",
            "details": "Es wurden keine bekannten Tracker im Quelltext gefunden.",
            "empfehlung": None,
        }

    tracker_liste = ", ".join(gefundene_tracker)
    if hat_consent:
        return {
            "ampel": "gelb",
            "titel": "Tracking & Cookies",
            "details": (
                f"Gefundene Dienste: {tracker_liste}. Ein Cookie-/Consent-Tool scheint vorhanden zu sein. "
                "Bitte prüfen, dass Tracker erst NACH der Einwilligung geladen werden."
            ),
            "empfehlung": {
                "kurztext": "Consent-Tool vorhanden — prüfen, ob Tracker wirklich erst nach Klick auf 'Akzeptieren' laden.",
                "schritte": [
                    "Im Browser Cookies löschen und die Seite neu laden.",
                    "Im Netzwerk-Tab der Browser-Entwicklertools prüfen: Werden externe Skripte (Google, Facebook, …) schon <em>vor</em> der Einwilligung geladen?",
                    "Falls ja: Im Consent-Tool (z.B. Borlabs Cookie, Complianz) die Skripte als 'gesperrt bis Einwilligung' markieren.",
                ],
                "snippets": [],
            },
        }
    return {
        "ampel": "rot",
        "titel": "Tracking & Cookies",
        "details": (
            f"Gefundene Dienste: {tracker_liste}. Es wurde KEIN Cookie-/Consent-Tool erkannt. "
            "Ohne Einwilligung ist das datenschutzrechtlich riskant (DSGVO)."
        ),
        "empfehlung": {
            "kurztext": "Ohne Einwilligung der Besucher dürfen Tracking-Dienste nicht geladen werden — das ist in der EU Pflicht.",
            "schritte": [
                "<strong>WordPress:</strong> Plugin <em>Borlabs Cookie</em> (kostenlose Basis-Version reicht) oder <em>Complianz</em> installieren.",
                "<strong>Andere Systeme:</strong> Dienst wie <em>Cookiebot</em> (kostenlos bis 500 Seiten) oder <em>consentmanager.net</em> einbinden.",
                "Alternativ: Externe Tracker (z.B. Google Analytics) vollständig entfernen und durch datenschutzfreundliche Tools wie <em>Matomo</em> (selbst gehostet) ersetzen.",
                "Nach Einrichtung: Seite im Inkognito-Modus testen — der Consent-Banner muss <em>vor</em> jedem externen Skript erscheinen.",
            ],
            "snippets": [],
        },
    }
