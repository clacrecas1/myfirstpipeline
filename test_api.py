import pytest

from app import app


@pytest.fixture
def cliente():
    app.config.update(TESTING=True)
    return app.test_client()


def test_health(cliente):
    respuesta = cliente.get("/health")
    assert respuesta.status_code == 200
    assert respuesta.get_json() == {"estado": "ok"}


def test_saludo_con_nombre(cliente):
    respuesta = cliente.get("/saludo", query_string={"nombre": "Claudia"})
    assert respuesta.status_code == 200
    assert respuesta.get_json()["saludo"].endswith("Claudia")


@pytest.mark.parametrize(
    "parametros",
    [{"nombre": "<script>alert(1)</script>"}, {"idioma": "fr"}],
)
def test_entrada_invalida_devuelve_400(cliente, parametros):
    assert cliente.get("/saludo", query_string=parametros).status_code == 400
