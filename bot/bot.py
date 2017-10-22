# -*- coding: utf-8 -*-

import telebot # Librería de la API del bot.
import time # Librería para hacer que el programa que controla el bot no se acabe.
from funciones import *
from telebot import types # Tipos para la API del bot.
import re
import os

bot = telebot.TeleBot(os.environ["token_bot"])

def listener(messages):
    for m in messages:
        if m.content_type == 'text': # Filtramos mensajes que sean tipo texto.
            cid = m.chat.id # Almacenaremos el ID de la conversación.
            print ("[" + str(cid) + "]: " + m.text)
            # Y haremos que imprima algo parecido a esto -> [42133876]: /start

bot.set_update_listener(listener)
# Así, le decimos al bot que utilice como función escuchadora nuestra función 'listener'
#declarada arriba.

@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    bot.send_message(cid, 'Lista de comandos: /start /buscar_track' )

@bot.message_handler(commands=['buscar_track'])
def command_buscar_track(m):
    datos = []
    cid = m.chat.id
    track = m.text
    track = track[14:]
    documento = cargarWeb(track)
    datos.append(nombreEmpresa(documento))
    datos.append(informacionMensaje(documento))
    datos.append(fechaMensaje(documento))
    bot.send_message(cid, 'Nombre de la empresa: ' + datos[0])
    for p in range(len(datos[1][0])):
        bot.send_message(cid, 'Fecha: ' + datos[2][p])
        bot.send_message(cid, 'Evento: ' + datos[1][0][p])

bot.polling(none_stop=True)
