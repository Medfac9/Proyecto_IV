from flask import Flask, request
from bot.funciones import *
import json

app = Flask(__name__)

@app.route("/")
def index():
    return ("Bienvenido")

@app.route("/track/<numero>")
def numero_track(numero):
    informacion = []
    documento = cargarWeb(numero)
    informacion.append(nombreEmpresa(documento))
    informacion.append(informacionMensaje(documento))
    informacion.append(fechaMensaje(documento))
    return json.dumps(informacion)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
