import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def comprobarTrack(numero_track):
    enlace = "http://www.17track.net/en/track?nums=" + numero_track
    driver = webdriver.Chrome()
    driver.get(enlace)
    html = driver.page_source
    documento = BeautifulSoup(html, "html5lib")

    existe = documento.find_all("span", class_ = "color-sky flag-status")[0].get_text()

    if(existe == "Not Found"):
        return -1

    empresa = documento.find_all("span", class_ = "jsTips express")[0].get_text()
    tamano = len(documento.find_all("div", class_ = "track-news clearfix"))
    mensajes = []
    fechas = []
    info = []

    for i in range(0,len(documento.find_all("div", class_ = "track-news clearfix"))):
        mensajes.append(documento.find_all("div", class_ = "track-news clearfix")[i].get_text())
        temp = mensajes[i]
        temp2 = mensajes[i]
        temp = temp[0:16]
        temp2 = temp2[17:]
        fechas.append(temp)
        info.append(temp2)

    return empresa, info, tamano, fechas

#nombre_empresa, info, tamano, fecha = comprobarTrack("PQ48K20440124700118006G")
nombre_empresa, info, tamano, fecha = comprobarTrack("GM295118118000047210")
print("Nombre de la empresa: " + nombre_empresa)
for i in range(tamano):
    print("\nFecha: " + fecha[i])
    print("\nInformación: " + info[i])
