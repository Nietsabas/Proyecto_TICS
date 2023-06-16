# Detector de Luz con Fotoresistor
## Descripción
Este proyecto fue desarrollado como parte del curso EL5207-1 Laboratorio de Tecnologías de Información y Comunicaciones semestre Otoño 2023. Consiste en un detector de luz que utiliza un fotoresistor para medir niveles de luminosidad y enviar los datos a una Raspberry Pi mediante un ESP8266. La Raspberry Pi procesa los datos y realiza acciones basadas en la intensidad de la luz detectada.

## Características
* Mide los niveles de luz utilizando un fotoresistor.
* Transmite los datos de luminosidad a la Raspberry Pi mediante el ESP8266.
* La Raspberry Pi procesa los datos y realiza acciones en función de la intensidad de la luz.



## Materiales y Componentes
* Fotoresistor
* Raspberry Pi
* ESP8266
* Resistencias 330 y 10k Ohms
* Led
* Protoboard
* Cables jumper

## Instrucciones de configuración
1. Conecta el fotoresistor y las resistencias en la breadboard según el esquema de conexión proporcionado en el archivo "connection_diagram.png" (incluido en el repositorio).
2. Conecta el ESP8266 a la Raspberry Pi mediante los pines GPIO correspondientes.
3. Sigue las instrucciones proporcionadas en el archivo "setup_instructions.md" (incluido en el repositorio) para configurar el entorno de desarrollo y las dependencias necesarias en la Raspberry Pi.
4. Verifica que el ESP8266 esté correctamente configurado y conectado a la red Wi-Fi.
5. Ejecuta el código del proyecto en la Raspberry Pi.

## Cómo utilizar
1. Enciende el sistema y espera a que se establezca la conexión entre la Raspberry Pi y el ESP8266.
2. El fotoresistor medirá continuamente los niveles de luz y enviará los datos a la Raspberry Pi.
3. La Raspberry Pi procesará los datos y realizará acciones basadas en la intensidad de la luz detectada.


## Contribución
Actualmente, este proyecto no acepta contribuciones externas. Sin embargo, si encuentras algún problema o tienes sugerencias, no dudes en crear un "issue" en el repositorio de GitHub.



## Autor
Este proyecto fue desarrollado por Bruno Araya y Sebastián Versluys. Puedes contactarme por correo electrónico en sebastian.versluys@ug.uchile.cl o bruno.araya.h@ug.uchile.cl.

## Agradecimientos
Agradecemos al curso EL5207-1 Laboratorio de Tecnologías de Información y Comunicaciones por proporcionar el contexto y los recursos necesarios para la realización de este proyecto.

## Foto de los autores

![Logo de mi proyecto](https://github.com/Nietsabas/Proyecto_TICS/blob/main/foto_autores.jpg)