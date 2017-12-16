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
        # nombre = informacion.append(nombreEmpresa(documento))
        # info = informacion.append(informacionMensaje(documento))
        # fecha = informacion.append(fechaMensaje(documento))

        schema = {
            "Nombre de la empresa de transporte": informacion.append(nombreEmpresa(documento)),
            "Fecha": informacion.append(fechaMensaje(documento)),
            "Evento": informacion.append(informacionMensaje(documento))
        }
        
        return jsonify(schema)

api.add_resource(Tracking, '/track/<numero>')

class status(Resource):
    def get(self):
        schema = {
           "status": "OK"
        }
        return jsonify(schema)

api.add_resource(status, '/')

class statusDocker(Resource):
    def get(self):
        schema = {
           "status": "OK"
        }
        return jsonify(schema)

api.add_resource(statusDocker, '/status')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
