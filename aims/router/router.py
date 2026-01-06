from langdetect import detect

SPANISH_HINTS = {
        "hola", "ayuda", "sesion", "sesión", "cuenta",
        "no puedo", "iniciar", "iniciar sesion", "iniciar sesión"
}

def route_message(text: str) -> str:
        t = text.lower()

        # Fast heuristic for Spanish
        if any(h in t for h in SPANISH_HINTS):
            return "language_es"

        try:
            lang = detect(text)
        except Exception:
            lang = "en"

        if lang.startswith("es"):
            return "language_es"

        return "language_en"
