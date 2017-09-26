# Proyecto IV
**Proyecto**: bot de telegram  
**Descrición**: El bot recibirá un número de track, el cual, será introducido en la web [17track](http://www.17track.net/) y nos mostrará dónde está nuestro paquete, la fechas de entrada y salida de la ciudad donde se encuentre y una breve descripción (el paquete ha sido enviado, en distribución, ...). Al número de track se le podrá poner un alias para facilitar al usuario. El bot avisará al cliente de cada cambio que se realice sobre su paquete.  
**Servicios**:  
* **Lenguaje**: Python
* **Base de datos**: Amazon Web Services (AWS)
* **Servidor de mensajería**: telegram
* **Sistema de ficheros específico**:
* **Compilador, librerías o aplicaciones externas determinadas**: requests (obtiene la informacion del sitio), BeautifulSoup (analiza el documento HTML obtenido) y re (trata las expresiones regulares que podamos encontrar en un documento HTML). La API que utilizaré para el desarrollo del proyecto será pyTelegramBotAPI.

**Problema que resuelve el bot**: Tener controlado en todo momento el movimiento de los paquetes sin la necesidad de hacer busquedas manuales del mismo.  
