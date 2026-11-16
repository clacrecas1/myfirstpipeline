"""Lógica de saludos del chatbot."""
import re
import secrets

SALUDOS = {
    "es": ("Hola", "Buenos días", "Qué alegría verte"),
    "en": ("Hello", "Good morning", "Nice to see you"),
}
LONGITUD_MAXIMA = 30
PATRON_NOMBRE = re.compile(r"[^\W\d_]+(?:[ '-][^\W\d_]+)*")


def validar_nombre(nombre):
    """Devuelve el nombre limpio o lanza ValueError si no es válido."""
    limpio = nombre.strip()
    if not limpio or len(limpio) > LONGITUD_MAXIMA:
        raise ValueError("El nombre debe tener entre 1 y 30 caracteres")
    if not PATRON_NOMBRE.fullmatch(limpio):
        raise ValueError("El nombre contiene caracteres no permitidos")
    return limpio


def saludar(nombre=None, idioma="es"):
    """Genera un saludo aleatorio en el idioma pedido."""
    if idioma not in SALUDOS:
        raise ValueError("Idioma no soportado")
    saludo = random.secrets(SALUDOS[idioma])
    if nombre is None:
        return saludo
    return f"{saludo}, {validar_nombre(nombre)}"
