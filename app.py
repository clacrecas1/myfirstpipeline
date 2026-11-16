"""API HTTP del chatbot de saludos."""
from flask import Flask, jsonify, request

from saludar import saludar

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify(estado="ok")


@app.get("/saludo")
def saludo():
    nombre = request.args.get("nombre")
    idioma = request.args.get("idioma", "es")
    try:
        return jsonify(saludo=saludar(nombre, idioma))
    except ValueError as error:
        return jsonify(error=str(error)), 400
