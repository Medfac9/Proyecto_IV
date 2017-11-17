[![Build Status](https://travis-ci.org/Medfac9/Proyecto_IV.svg?branch=master)](https://travis-ci.org/Medfac9/Proyecto_IV)   
![](https://dockerbuildbadges.quelltext.eu/status.svg?organization=Medfac9&repository=Proyecto_IV)  
[![codecov.io Code Coverage](https://img.shields.io/codecov/c/github/Medfac9/Proyecto_IV.svg)](https://codecov.io/gh/Medfac9/Proyecto_IV)  
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)  
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Medfac9/Proyecto_IV)

# Proyecto IV
**Proyecto**: Bot de telegram  
**Nombre del bot**: @TrackBot  
**Descrición**: El bot recibirá un número de track, el cual, será introducido en la web [17track](http://www.17track.net/) y nos mostrará dónde está nuestro paquete, la fechas de entrada y salida de la ciudad donde se encuentre y una breve descripción (el paquete ha sido enviado, en distribución, ...). Al número de track se le podrá poner un alias para facilitar al usuario. El bot avisará al cliente de cada cambio que se realice sobre su paquete.  

**Servicios**:  
* **Lenguaje**: Python
* **Base de datos**: Amazon Web Services (AWS)
* **Servidor de mensajería**: telegram
* **Compilador, librerías o aplicaciones externas determinadas**: requests (obtiene la informacion del sitio), BeautifulSoup (analiza el documento HTML obtenido), re (trata las expresiones regulares que podamos encontrar en un documento HTML) y selenium (obtener información de una web de forma dinámica). La API que utilizaré para el desarrollo del proyecto será pyTelegramBotAPI.

**Problema que resuelve el bot**: Tener controlado en todo momento el movimiento de los paquetes sin la necesidad de hacer busquedas manuales del mismo.  

**¿Por qué sistema de test y de integración continua?**: El sistema de test consiste en un proceso que detecta si hay cambios en el código. Si es así, los cambios deben de pasar unos test predefinidos, los cuales, se encargan de ver si el código nuevo cumple los requisitos deseados. A este proceso lo llamamos integración continua. Esto es útil para evitar fallos y posibles complicaciones en el futuro.

**PaaS elegido**: El PaaS elegido es Heroku. He elegido dicho PaaS gracias a la facilidad de su uso y además nos da la posibilidad de integrar una base de datos basada en Postgres. También nos permite alojar nuestra aplicación de forma gratuita.

**Despliegue en Heroku**: Para desplegar nuestra aplicación será necesario usar los siguientes ficheros:
* **Procfile**: Se situa en la raíz y contiene los comandos necesarios para ejecutar el bot.
* **runtime.txt**: Se situa en la raíz y contiene el lenguaje y versión de nuestra aplicación.

A continuación creamos la aplicación en Heroku con el comando `heroku create --region eu -a 'nombre_app'` y una base de datos`heroku addons:create heroku-postgresql:hobby-basic -a 'nombre_app'`. Seguidamente, enlazamos nuestra aplicación en Heroku con nuestro repositorio de GitHub.

Para finalizar, activamos la opción de despliegue automatico en Heroku en la pestaña Deploy.

Estas son algunas imagenes del despliegue en Heroku:

![Captura de pantalla1](https://imgur.com/ooRurRc.jpg)

![Captura de pantalla2](https://imgur.com/On3dZ70.jpg)

![Captura de pantalla3](https://imgur.com/qqdqVr6.jpg)

Despliegue https://track-bot-api.herokuapp.com/

**Despliegue en Docker**: Primeramente creamos nuestro repositorio en Docker y lo enlazamos con GitHub

![Captura de pantalla4](https://imgur.com/tkfk9fy.jpg)

![Captura de pantalla5](https://imgur.com/9f8GAQP.jpg)

Seguidamente, crearemos un archivo Dockerfile que incluiremos en nuestro repositorio. Si todo está bien configurado, Docker construirá un contenedor. Una vez acabado, vemos que no ha ocurrido ningún error:

![Captura de pantalla6](https://imgur.com/Z9dLq5E.jpg)

Con el sigueinte comando: `sudo docker run -e "token_bot=MI_TOKEN" -i -t medfac9/track-bot` tendremos acceso a nuestro contenedor y podremos ejecutar nuestra aplicación desde Docker.

Se puede acceder al repositorio de Docker por el siguiente enlace: https://hub.docker.com/r/medfac9/track-bot/