# Proyecto de Título UNAB
Gonzalo Contreras Caneo

Se encontraran todos los archivos que son necesarios para la instalacion y puesta en funcionamiento del proyecto realizado por el estudiante Gonzalo Contreras para la Universidad Andres Bello.

GUÍA INSTALACIÓN

Para la instalación y puesta en funcionamiento de este proyecto, se deben seguir una serie de pasos para que se logra levantar el servidor de forma correcta.
Instalación del software.
  •	Visitar la página ev3dev.org
  
  •	Descargar la última versión de ev3dev
  
  •	Instalarla en una tarjeta microSD de no más de 16GB en forma de boot
  
  •	Insertar la tarjeta en el robot
  
  •	Esperar a que cargue e inicie el sistema operativo
  
Para el levantamiento del servidor se necesita que estén guardados diferentes códigos

  •	Descargar programa que logre hacer una comunicación por SSH con el robot, por ejemplo, MobaXterm
  
  •	Luego de lograr la conexión, en el mismo SSH, escribir en el terminal unas líneas para actualizar el EV3:
  
    o	sudo apt-get upgrade
    
    o	sudo apt-get install python-ev3dev
    
  •	Luego de hacer la conexión, pasar los códigos que están en la carpeta.
  
  Para levantar el servidor solo basta con ejecutar el código desde el mismo SSH escribiendo:
  
  •	python http.py
  
Para instalar la segunda parte, es necesario instalar la librería RPyC en el EV3 a través del mismo SSH y en su terminal escribir:

  •	sudo easy_install3 rpyc
  
Crear un archivo en le mismo EV3 y guardarlo en formato .sh y dentro de este escribir la línea de código:

  #!/bin/bash
  python3 `which rpyc_classic.py`


Y desde el mismo terminal del SSH ejecutarlo con la línea:

•	./rpyc_server.sh (depende del nombre que le hayas puesto al archivo, en mi caso, rpyc_server)




