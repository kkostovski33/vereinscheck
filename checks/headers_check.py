"""Security-Header-Check: Setzt die Website die wichtigsten Schutz-Header?"""

WICHTIGE_HEADER = {
    "strict-transport-security": "HSTS (erzwingt HTTPS im Browser)",
    "content-security-policy": "CSP (Schutz vor eingeschleustem Code)",
    "x-frame-options": "X-Frame-Options (Schutz vor Clickjacking)",
    "x-content-type-options": "X-Content-Type-Options (verhindert MIME-Tricks)",
    "referrer-policy": "Referrer-Policy (weniger Datenabfluss beim Weiterklicken)",
}

_SNIPPET_HTACCESS = """\
# Am Anfang eurer .htaccess-Datei einfügen:
<IfModule mod_headers.c>
    Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains"
    Header always set X-Frame-Options "SAMEORIGIN"
    Header always set X-Content-Type-Options "nosniff"
    Header always set Referrer-Policy "strict-origin-when-cross-origin"
    Header always set Content-Security-Policy "default-src 'self'"
</IfModule>"""

_SNIPPET_NGINX = """\
# Im server {}-Block eurer nginx.conf einfügen:
add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
add_header X-Frame-Options "SAMEORIGIN" always;
add_header X-Content-Type-Options "nosniff" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
add_header Content-Security-Policy "default-src 'self'" always;"""

_SNIPPET_WP = """\
// In der functions.php eures Child-Themes einfügen:
add_action('send_headers', function () {
    header('Strict-Transport-Security: max-age=31536000; includeSubDomains');
    header('X-Frame-Options: SAMEORIGIN');
    header('X-Content-Type-Options: nosniff');
    header('Referrer-Policy: strict-origin-when-cross-origin');
});
// Tipp: Das kostenlose Plugin "HTTP Headers" erledigt das ohne Code."""


def check_headers(response) -> dict:
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
        return {
            "ampel": "gruen",
            "titel": "Security-Header",
            "details": "Alle 5 Sicherheits-Einstellungen sind aktiv. Gut gemacht!",
            "empfehlung": None,
        }

    if anzahl >= 3:
        ampel = "gelb"
        text = f"{anzahl} von 5 Sicherheits-Einstellungen aktiv — {len(fehlend)} fehlen noch. Die Website ist grundlegend geschützt, aber nicht optimal."
    else:
        ampel = "rot"
        text = f"Nur {anzahl} von 5 Sicherheits-Einstellungen aktiv — {len(fehlend)} fehlen. Das macht die Website leichter angreifbar."

    return {
        "ampel": ampel,
        "titel": "Security-Header",
        "details": text,
        "empfehlung": {
            "kurztext": "Diese Sicherheits-Einstellungen fehlen noch: " + ", ".join(fehlend) + ". Sie lassen sich in wenigen Minuten per Konfigurationsdatei oder Plugin setzen — ohne Programmierkenntnisse.",
            "schritte": [
                "Welches System nutzt eure Website? <em>Das ist wichtig, weil der Code je nach System (WordPress, Apache, nginx) an einer anderen Stelle eingetragen wird.</em> Ihr findet das oft im Hoster-Panel oder könnt euren Webmaster fragen.",
                "Den passenden Code-Schnipsel unten kopieren und eintragen — oder einfach dem Webmaster schicken. <em>Der Schnipsel sagt dem Server, welche Schutzregeln er für alle Besucher durchsetzen soll. Einmal gesetzt, läuft das automatisch.</em>",
                "Kostenlos auf <strong><a href='https://securityheaders.com' target='_blank' rel='noopener'>securityheaders.com</a></strong> prüfen. <em>So seht ihr sofort ohne Technik-Wissen, ob die Einstellungen aktiv sind — grüne Punkte bedeuten: erledigt.</em>",
            ],
            "snippets": [
                {
                    "label": "Apache / WordPress (.htaccess)",
                    "lang": "apache",
                    "code": _SNIPPET_HTACCESS,
                },
                {
                    "label": "nginx (nginx.conf)",
                    "lang": "nginx",
                    "code": _SNIPPET_NGINX,
                },
                {
                    "label": "WordPress (functions.php)",
                    "lang": "php",
                    "code": _SNIPPET_WP,
                },
            ],
        },
    }
