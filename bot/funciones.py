import requests
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

def cargarWeb(numero_track):
    desired_cap = {
        'platform': "Linux",
        'browserName': "chrome",
        'version': "48.0",
     }
    driver = webdriver.Remote(command_executor='http://dmrh:9b85933b-c43b-4394-9e31-140ec0cb793d@ondemand.saucelabs.com:80/wd/hub', desired_capabilities=desired_cap)
    enlace = "http://www.17track.net/en/track?nums=" + numero_track
    driver.get(enlace)
    html = driver.page_source
    documento = BeautifulSoup(html, "html5lib")
    driver.quit()
    return documento

def nombreEmpresa(documento):
    existe = documento.find_all("span", class_ = "color-sky flag-status")[0].get_text()
    if(existe == "Not Found"):
        return None

    empresa = documento.find_all("span", class_ = "jsTips express")[0].get_text()

    return empresa

def informacionMensaje(documento):
    existe = documento.find_all("span", class_ = "color-sky flag-status")[0].get_text()
    if(existe == "Not Found"):
        return None

    tamano = len(documento.find_all("div", class_ = "track-news clearfix"))
    mensajes = []
    info = []

    for i in range(0,len(documento.find_all("div", class_ = "track-news clearfix"))):
        mensajes.append(documento.find_all("div", class_ = "track-news clearfix")[i].get_text())
        temp = mensajes[i]
        temp = temp[17:]
        info.append(temp)

    return info, tamano

def fechaMensaje(documento):
    existe = documento.find_all("span", class_ = "color-sky flag-status")[0].get_text()

    if(existe == "Not Found"):
        return None

    tamano = len(documento.find_all("div", class_ = "track-news clearfix"))
    mensajes = []
    fechas = []

    for i in range(0,len(documento.find_all("div", class_ = "track-news clearfix"))):
        mensajes.append(documento.find_all("div", class_ = "track-news clearfix")[i].get_text())
        temp = mensajes[i]
        temp = temp[0:16]
        fechas.append(temp)

    return fechas
