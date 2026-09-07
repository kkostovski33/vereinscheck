"""PDF-Bericht-Generator für VereinsCheck.

Erzeugt einen professionellen Sicherheitsbericht,
den Vereinsvorstände direkt an ihren Webmaster schicken können.
"""

from datetime import datetime
from fpdf import FPDF

# Ampel → deutsche Bezeichnung + RGB-Farbe
AMPEL_CONFIG = {
    "gruen": {"label": "OK",      "rgb": (34,  197, 94)},
    "gelb":  {"label": "Hinweis", "rgb": (234, 179, 8)},
    "rot":   {"label": "Problem", "rgb": (239, 68,  68)},
}

NAVY   = (15,  23, 42)
BLAU   = (3,  105, 161)
GRAU   = (71,  85, 105)
HELL   = (241, 245, 249)
WEISS  = (255, 255, 255)
BORDER = (226, 232, 240)


FONT_PATH = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf"


class BerichtPDF(FPDF):
    def __init__(self, domain: str):
        super().__init__()
        self.domain = domain
        self.datum  = datetime.now().strftime("%d. %B %Y").replace(
            "January","Januar").replace("February","Februar").replace(
            "March","März").replace("April","April").replace(
            "May","Mai").replace("June","Juni").replace(
            "July","Juli").replace("August","August").replace(
            "September","September").replace("October","Oktober").replace(
            "November","November").replace("December","Dezember")
        self.set_auto_page_break(auto=True, margin=20)
        # Unicode-Schrift laden (Regular + Bold über dasselbe File, fpdf2 emuliert Bold)
        self.add_font("Arial", style="",  fname=FONT_PATH)
        self.add_font("Arial", style="B", fname=FONT_PATH)
        self.add_font("Arial", style="I", fname=FONT_PATH)

    def header(self):
        # Blauer Balken oben
        self.set_fill_color(*NAVY)
        self.rect(0, 0, 210, 14, "F")
        self.set_y(3)
        self.set_font("Arial", "B", 11)
        self.set_text_color(*WEISS)
        self.cell(0, 8, "VereinsCheck  |  Sicherheitsbericht", align="L", new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(*NAVY)
        self.ln(4)

    def footer(self):
        self.set_y(-14)
        self.set_font("Arial", "", 8)
        self.set_text_color(*GRAU)
        self.cell(0, 6, f"VereinsCheck  ·  vereinscheck.de  ·  Seite {self.page_no()}", align="C")

    # ── Helpers ──────────────────────────────────────────────────

    def h1(self, text: str):
        self.set_font("Arial", "B", 18)
        self.set_text_color(*NAVY)
        self.cell(0, 10, text, new_x="LMARGIN", new_y="NEXT")
        self.ln(1)

    def h2(self, text: str):
        self.set_font("Arial", "B", 12)
        self.set_text_color(*BLAU)
        self.cell(0, 8, text, new_x="LMARGIN", new_y="NEXT")

    def body(self, text: str, color=None):
        self.set_font("Arial", "", 10)
        self.set_text_color(*(color or GRAU))
        self.multi_cell(0, 6, text)
        self.ln(1)

    def divider(self, margin_top: float = 3, margin_bottom: float = 3):
        self.ln(margin_top)
        self.set_draw_color(*BORDER)
        self.set_line_width(0.3)
        self.line(self.l_margin, self.get_y(), 210 - self.r_margin, self.get_y())
        self.ln(margin_bottom)

    def badge(self, label: str, rgb: tuple):
        """Farbige Statusmarke (z.B. OK / Hinweis / Problem)."""
        w = 22
        self.set_fill_color(*rgb)
        self.set_text_color(*WEISS)
        self.set_font("Arial", "B", 8)
        self.cell(w, 6, label, border=0, align="C", fill=True,
                  new_x="RIGHT", new_y="LAST")
        self.set_text_color(*NAVY)

    def code_block(self, code: str):
        """Grauer Hintergrund-Block für Code-Snippets."""
        self.set_fill_color(*HELL)
        self.set_draw_color(*BORDER)
        self.set_font("Arial", "", 8)
        self.set_text_color(*NAVY)
        self.set_line_width(0.3)
        lines = code.split("\n")
        block_h = len(lines) * 4.5 + 4
        x, y = self.get_x(), self.get_y()
        self.rect(x, y, 170, block_h, "FD")
        self.set_xy(x + 2, y + 2)
        for line in lines:
            self.cell(166, 4.5, line, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    # ── Seitenaufbau ─────────────────────────────────────────────

    def seite_deckblatt(self):
        self.add_page()

        # Titel
        self.ln(4)
        self.h1(f"Sicherheitsbericht")
        self.set_font("Arial", "", 13)
        self.set_text_color(*BLAU)
        self.cell(0, 7, self.domain, new_x="LMARGIN", new_y="NEXT")
        self.set_font("Arial", "", 10)
        self.set_text_color(*GRAU)
        self.cell(0, 6, f"Erstellt am {self.datum} mit VereinsCheck",
                  new_x="LMARGIN", new_y="NEXT")

        self.divider(margin_top=6, margin_bottom=6)

        # Anschreiben
        self.h2("Sehr geehrtes Webmaster-Team,")
        self.ln(2)
        self.body(
            f"im Rahmen eines kostenlosen IT-Sicherheits-Checks der Website {self.domain} "
            f"wurden die folgenden Punkte festgestellt. Dieser Bericht wurde automatisch "
            f"von VereinsCheck generiert.\n\n"
            f"Bitte prüft die markierten Punkte und nehmt — wo möglich — die empfohlenen "
            f"Änderungen vor. Zu jedem Problem findet ihr weiter unten eine konkrete "
            f"Schritt-für-Schritt-Anleitung sowie fertige Code-Snippets zum Einfügen.\n\n"
            f"Bei Fragen stehen wir euch gerne zur Verfügung.",
            color=NAVY
        )

        self.ln(2)
        self.set_font("Arial", "", 10)
        self.set_text_color(*GRAU)
        self.cell(0, 6, "Mit freundlichen Grüßen,", new_x="LMARGIN", new_y="NEXT")
        self.set_font("Arial", "B", 10)
        self.set_text_color(*NAVY)
        self.cell(0, 6, "Der Vereinsvorstand", new_x="LMARGIN", new_y="NEXT")

    def seite_ergebnisse(self, ergebnisse: list):
        self.add_page()
        self.h1("Übersicht der Ergebnisse")
        self.divider(margin_top=2, margin_bottom=4)

        for e in ergebnisse:
            cfg   = AMPEL_CONFIG[e["ampel"]]
            start_y = self.get_y()

            # Status-Badge links
            self.badge(cfg["label"], cfg["rgb"])
            self.set_x(self.l_margin + 26)

            # Titel
            self.set_font("Arial", "B", 10)
            self.set_text_color(*NAVY)
            self.cell(0, 6, e["titel"], new_x="LMARGIN", new_y="NEXT")

            # Details
            self.set_x(self.l_margin + 4)
            self.set_font("Arial", "", 9)
            self.set_text_color(*GRAU)
            self.multi_cell(160, 5, e["details"])

            self.ln(3)
            self.divider(margin_top=0, margin_bottom=4)

    def seite_loesungen(self, ergebnisse: list):
        """Seite(n) mit detaillierten Lösungsanleitungen für jedes Problem."""
        probleme = [e for e in ergebnisse if e.get("empfehlung")]
        if not probleme:
            return

        self.add_page()
        self.h1("Schritt-für-Schritt-Anleitungen")
        self.body("Für jedes Problem findet ihr hier die konkreten Schritte zur Behebung.", color=GRAU)
        self.divider(margin_top=2, margin_bottom=4)

        for e in probleme:
            emp = e["empfehlung"]
            cfg = AMPEL_CONFIG[e["ampel"]]

            # Bereich-Überschrift mit Badge
            self.badge(cfg["label"], cfg["rgb"])
            self.set_x(self.l_margin + 26)
            self.set_font("Arial", "B", 11)
            self.set_text_color(*NAVY)
            self.cell(0, 6, e["titel"], new_x="LMARGIN", new_y="NEXT")
            self.ln(1)

            # Kurztext
            self.set_font("Arial", "I", 9)
            self.set_text_color(*GRAU)
            self.multi_cell(0, 5, emp["kurztext"])
            self.ln(3)

            # Schritte
            self.set_font("Arial", "B", 9)
            self.set_text_color(*BLAU)
            self.cell(0, 5, "Was tun?", new_x="LMARGIN", new_y="NEXT")
            self.ln(1)

            for i, schritt in enumerate(emp["schritte"], 1):
                # HTML-Tags entfernen für die PDF
                clean = _strip_html(schritt)
                self.set_fill_color(*BLAU)
                self.set_text_color(*WEISS)
                self.set_font("Arial", "B", 8)
                self.cell(6, 5, str(i), fill=True, align="C",
                          new_x="RIGHT", new_y="LAST")
                self.set_x(self.l_margin + 8)
                self.set_font("Arial", "", 9)
                self.set_text_color(*NAVY)
                self.multi_cell(162, 5, clean)
                self.ln(1)

            # Code-Snippets
            if emp.get("snippets"):
                self.ln(2)
                self.set_font("Arial", "B", 9)
                self.set_text_color(*BLAU)
                self.cell(0, 5, "Code-Beispiele zum Einfügen:", new_x="LMARGIN", new_y="NEXT")
                self.ln(1)
                for s in emp["snippets"]:
                    self.set_font("Arial", "B", 8)
                    self.set_text_color(*GRAU)
                    self.cell(0, 4, s["label"], new_x="LMARGIN", new_y="NEXT")
                    self.ln(1)
                    self.code_block(s["code"])
                    self.ln(1)

            self.divider(margin_top=4, margin_bottom=6)


def erstelle_bericht(domain: str, ergebnisse: list) -> bytes:
    """Gibt den fertigen PDF-Bericht als Bytes zurück."""
    pdf = BerichtPDF(domain)
    pdf.seite_deckblatt()
    pdf.seite_ergebnisse(ergebnisse)
    pdf.seite_loesungen(ergebnisse)
    return bytes(pdf.output())


def _strip_html(text: str) -> str:
    """Entfernt einfache HTML-Tags für die PDF-Ausgabe."""
    import re
    text = re.sub(r"<[^>]+>", "", text)
    text = text.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    return text
