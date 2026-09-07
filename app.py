"""VereinsCheck – Flask-Web-Interface."""

from urllib.parse import urlparse

from flask import Flask, render_template, request, Response

from checks.ssl_check import check_ssl
from checks.headers_check import check_headers
from checks.tracking_check import check_tracking
from checks.form_check import check_forms
from bericht import erstelle_bericht
import requests as req_lib

app = Flask(__name__)

def _read_version() -> str:
    try:
        with open("VERSION") as f:
            return f.read().strip()
    except FileNotFoundError:
        return "0.0.0"

APP_VERSION = _read_version()

@app.context_processor
def inject_version():
    return {"app_version": APP_VERSION}


def _scan(url_eingabe: str):
    """Führt alle Checks durch und gibt (ergebnisse, hostname) zurück."""
    url      = normalisiere_url(url_eingabe)
    hostname = urlparse(url).hostname
    if not hostname:
        return None, None

    ergebnisse = [check_ssl(hostname)]
    antwort    = hole_seite(url)
    if antwort is not None:
        ergebnisse.append(check_headers(antwort))
        ergebnisse.append(check_tracking(antwort.text))
        ergebnisse.append(check_forms(antwort.text, antwort.url))
    else:
        for titel in ("Security-Header", "Tracking & Cookies", "Formular-Sicherheit"):
            ergebnisse.append({
                "ampel": "gelb", "titel": titel,
                "details": "Konnte nicht geprüft werden – Seite nicht erreichbar.",
                "empfehlung": None,
            })
    return ergebnisse, hostname


def normalisiere_url(eingabe: str) -> str:
    eingabe = eingabe.strip()
    if not eingabe.startswith(("http://", "https://")):
        eingabe = "https://" + eingabe
    return eingabe


def hole_seite(url: str):
    try:
        return req_lib.get(
            url,
            timeout=15,
            headers={"User-Agent": "VereinsCheck/0.1"},
            allow_redirects=True,
        )
    except req_lib.RequestException:
        return None


@app.route("/", methods=["GET", "POST"])
def index():
    ergebnisse = None
    url_eingabe = ""
    fehler = None
    fazit = None

    if request.method == "POST":
        url_eingabe = request.form.get("url", "").strip()
        if not url_eingabe:
            fehler = "Bitte eine Website-Adresse eingeben."
        else:
            url = normalisiere_url(url_eingabe)
            hostname = urlparse(url).hostname
            if not hostname:
                fehler = "Das sieht nicht wie eine gültige Website-Adresse aus."
            else:
                ergebnisse, _ = _scan(url_eingabe)

                if any(e["ampel"] == "rot" for e in ergebnisse):
                    fazit = ("rot", "Es gibt dringenden Handlungsbedarf (rote Punkte oben).")
                elif any(e["ampel"] == "gelb" for e in ergebnisse):
                    fazit = ("gelb", "Grundsätzlich ok, aber es gibt Verbesserungspunkte.")
                else:
                    fazit = ("gruen", "Sehr gut – alle Basis-Checks sind grün!")

    return render_template(
        "index.html",
        ergebnisse=ergebnisse,
        url_eingabe=url_eingabe,
        fehler=fehler,
        fazit=fazit,
    )


@app.route("/datenschutz")
def datenschutz():
    return render_template("datenschutz.html")


@app.route("/bericht", methods=["POST"])
def bericht():
    url_eingabe = request.form.get("url", "").strip()
    if not url_eingabe:
        return "Keine URL angegeben.", 400

    ergebnisse, hostname = _scan(url_eingabe)
    if ergebnisse is None:
        return "Ungültige URL.", 400

    pdf_bytes = erstelle_bericht(hostname, ergebnisse)
    dateiname = f"VereinsCheck_{hostname.replace('.', '_')}.pdf"

    return Response(
        pdf_bytes,
        mimetype="application/pdf",
        headers={"Content-Disposition": f'attachment; filename="{dateiname}"'},
    )


if __name__ == "__main__":
    app.run(debug=True, port=8080)
