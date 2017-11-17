FROM ubuntu:16.04

MAINTAINER Rafael Medina Facal

# Variables de entorno para la conexion a la BD y para el Bot
ARG token_bot

ENV token_bot=$token_bot


RUN apt-get update
RUN apt-get install -y python3-pip
RUN apt-get install -y git
RUN git clone https://github.com/Medfac9/Proyecto_IV
RUN cd Proyecto_IV/ && pip3 install -r requirements.txt
EXPOSE 80
WORKDIR Proyecto_IV/

CMD ["gunicorn", "--config=config_gunicorn.py", "flask_api:app"]