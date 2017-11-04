[![Build Status](https://travis-ci.org/Medfac9/Proyecto_IV.svg?branch=master)](https://travis-ci.org/Medfac9/Proyecto_IV)  
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

**Despliegue del PaaS**: Para desplegar nuestra aplicación será necesario usar los siguientes ficheros:
* **Procfile**: Se situa en la raíz y contiene los comandos necesarios para ejecutar el bot.
* **runtime.txt**: Se situa en la raíz y contiene el lenguaje y versión de nuestra aplicación.

A continuación creamos la aplicación en Heroku con el comando `heroku create --region eu -a 'nombre_app'` y una base de datos`heroku addons:create heroku-postgresql:hobby-basic -a 'nombre_app'`. Seguidamente, enlazamos nuestra aplicación en Heroku con nuestro repositorio de GitHub.

Para finalizar, activamos la opción de despliegue automatico en Heroku en la pestaña Deploy.

Despliegue https://track-bot-api.herokuapp.com/
