"""SSL/TLS-Check: Ist die Website ueber HTTPS erreichbar und das Zertifikat gueltig?"""

import ssl
import socket
from datetime import datetime, timezone


def check_ssl(hostname: str, port: int = 443, timeout: float = 10.0) -> dict:
    """Prueft das TLS-Zertifikat einer Domain.

    Rueckgabe: dict mit 'ampel' (gruen/gelb/rot), 'titel' und 'details'.
    """
    context = ssl.create_default_context()
    try:
        with socket.create_connection((hostname, port), timeout=timeout) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
    except ssl.SSLCertVerificationError as exc:
        return {
            "ampel": "rot",
            "titel": "HTTPS-Verschlüsselung",
            "details": f"Das Zertifikat ist ungültig oder nicht vertrauenswürdig ({exc.reason}).",
            "empfehlung": {
                "kurztext": "Ohne gültiges Zertifikat sehen Besucher eine Sicherheitswarnung und verlassen die Seite.",
                "schritte": [
                    "Im Hosting-Panel ein neues SSL-Zertifikat aktivieren — bei den meisten Hostern kostenlos über <strong>Let's Encrypt</strong>.",
                    "Sicherstellen, dass die Domain exakt übereinstimmt (www vs. ohne www).",
                    "Nach Aktivierung: Browser-Cache leeren und erneut prüfen.",
                ],
                "snippets": [],
            },
        }
    except (socket.timeout, socket.gaierror, ConnectionRefusedError, OSError) as exc:
        return {
            "ampel": "rot",
            "titel": "HTTPS-Verschlüsselung",
            "details": f"Keine sichere HTTPS-Verbindung möglich ({exc}).",
            "empfehlung": {
                "kurztext": "Die Website ist entweder nicht erreichbar oder bietet kein HTTPS an.",
                "schritte": [
                    "Im Hosting-Panel prüfen, ob HTTPS / SSL aktiviert ist.",
                    "Sicherstellen, dass die Domain korrekt eingetragen ist.",
                    "Falls die Website neu ist: 24 Stunden warten, bis DNS sich propagiert hat.",
                ],
                "snippets": [],
            },
        }

    not_after = cert.get("notAfter")
    try:
        expires = datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z").replace(tzinfo=timezone.utc)
    except (TypeError, ValueError):
        return {
            "ampel": "gelb",
            "titel": "HTTPS-Verschlüsselung",
            "details": "HTTPS ist aktiv, das Ablaufdatum konnte aber nicht gelesen werden.",
            "empfehlung": None,
        }

    tage_uebrig = (expires - datetime.now(timezone.utc)).days

    if tage_uebrig < 0:
        return {
            "ampel": "rot",
            "titel": "HTTPS-Verschlüsselung",
            "details": f"Das Zertifikat ist seit {abs(tage_uebrig)} Tagen abgelaufen!",
            "empfehlung": {
                "kurztext": "Ein abgelaufenes Zertifikat schreckt Besucher ab und schadet dem Vertrauen. Sofort erneuern.",
                "schritte": [
                    "Im Hosting-Panel (z.B. IONOS, Strato, Hetzner) unter <strong>SSL/TLS</strong> das Zertifikat erneuern.",
                    "Bei den meisten Hostern ist <strong>Let's Encrypt</strong> kostenlos und verlängert sich automatisch.",
                    "Falls ihr einen eigenen Server betreibt: <code>certbot renew</code> ausführen.",
                ],
                "snippets": [],
            },
        }
    if tage_uebrig <= 21:
        return {
            "ampel": "gelb",
            "titel": "HTTPS-Verschlüsselung",
            "details": f"HTTPS ist aktiv, aber das Zertifikat läuft in {tage_uebrig} Tagen ab. Bald erneuern.",
            "empfehlung": {
                "kurztext": "Jetzt erneuern, bevor Besucher eine Sicherheitswarnung sehen.",
                "schritte": [
                    "Im Hosting-Panel unter <strong>SSL/TLS</strong> das Zertifikat verlängern.",
                    "Tipp: <strong>Auto-Verlängerung</strong> aktivieren, damit das nie wieder passiert.",
                ],
                "snippets": [],
            },
        }
    return {
        "ampel": "gruen",
        "titel": "HTTPS-Verschlüsselung",
        "details": f"HTTPS ist aktiv und das Zertifikat ist noch {tage_uebrig} Tage gültig.",
        "empfehlung": None,
    }
