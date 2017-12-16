from flask import Flask, request, jsonify
from bot.funciones import *
import json
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Tracking(Resource):
    def get(self, numero):
        documento = cargarWeb(numero)
        nombre = nombreEmpresa(documento)
        info = informacionMensaje(documento)
        fecha = fechaMensaje(documento)

        schema = {
            "Nombre de la empresa de transporte": nombreEmpresa(documento),
            "Fecha": fecha,
            "Evento": info
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
    app.run(debug=True, use_reloader=True)
