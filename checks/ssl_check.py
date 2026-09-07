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
            "titel": "HTTPS-Verschluesselung",
            "details": f"Das Zertifikat ist ungueltig oder nicht vertrauenswuerdig ({exc.reason}).",
        }
    except (socket.timeout, socket.gaierror, ConnectionRefusedError, OSError) as exc:
        return {
            "ampel": "rot",
            "titel": "HTTPS-Verschluesselung",
            "details": f"Keine sichere HTTPS-Verbindung moeglich ({exc}).",
        }

    # Ablaufdatum auslesen und Restlaufzeit berechnen
    not_after = cert.get("notAfter")
    try:
        expires = datetime.strptime(not_after, "%b %d %H:%M:%S %Y %Z").replace(tzinfo=timezone.utc)
    except (TypeError, ValueError):
        return {
            "ampel": "gelb",
            "titel": "HTTPS-Verschluesselung",
            "details": "HTTPS ist aktiv, das Ablaufdatum konnte aber nicht gelesen werden.",
        }

    tage_uebrig = (expires - datetime.now(timezone.utc)).days

    if tage_uebrig < 0:
        return {
            "ampel": "rot",
            "titel": "HTTPS-Verschluesselung",
            "details": f"Das Zertifikat ist seit {abs(tage_uebrig)} Tagen abgelaufen!",
        }
    if tage_uebrig <= 21:
        return {
            "ampel": "gelb",
            "titel": "HTTPS-Verschluesselung",
            "details": f"HTTPS ist aktiv, aber das Zertifikat laeuft in {tage_uebrig} Tagen ab. Bald erneuern.",
        }
    return {
        "ampel": "gruen",
        "titel": "HTTPS-Verschluesselung",
        "details": f"HTTPS ist aktiv und das Zertifikat ist noch {tage_uebrig} Tage gueltig.",
    }
