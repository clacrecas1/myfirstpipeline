import pytest

import saludar


@pytest.mark.parametrize("idioma", ["es", "en"])
def test_saludo_pertenece_al_idioma(idioma):
    assert saludar.saludar(idioma=idioma) in saludar.SALUDOS[idioma]


def test_saludo_incluye_nombre():
    assert saludar.saludar("Claudia").endswith(", Claudia")


def test_nombre_se_limpia():
    assert saludar.validar_nombre("  Ana María ") == "Ana María"


@pytest.mark.parametrize(
    "nombre",
    ["", "   ", "a" * 31, "<script>", "x' OR '1'='1", "Ana123", "../etc"],
)
def test_nombre_invalido(nombre):
    with pytest.raises(ValueError):
        saludar.validar_nombre(nombre)


def test_idioma_no_soportado():
    with pytest.raises(ValueError):
        saludar.saludar(idioma="fr")
