from flask import Flask, request, jsonify
from bot.funciones import *
import json
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Tracking(Resource):
    def get(self, numero):
        informacion = []
        documento = cargarWeb(numero)
        informacion.append(nombreEmpresa(documento))
        informacion.append(informacionMensaje(documento))
        informacion.append(fechaMensaje(documento))
        return informacion

api.add_resource(Tracking, '/track/<numero>')

class status(Resource):
    def get(self):
        schema = {
           "status": "OK",
           "ejemplo": { "ruta": "/check",
                        "valor": "{JSON: devuelto}"
                      }
        }
        return jsonify(schema)

api.add_resource(status, '/check')

@app.route("/")
def index():
    return ("Bienvenido")

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
