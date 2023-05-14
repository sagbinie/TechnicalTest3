# Geocodificación de direcciones

Este proyecto utiliza la API de Google Maps para geocodificar la dirección escrita y determina el vecindario correspondiente. Para ejecutar el archivo, es necesario tener instalados los siguientes módulos:

- googlemaps
- dotenv

## Puedes instalar los módulos requeridos ejecutando el siguiente comando:

```
pip3 install googlemaps python-dotenv
```

## Configuración de la clave de la API

Para utilizar la API de Google Maps, necesitarás generar una clave de API desde tu cuenta de Google Cloud Platform. A continuación, sigue estos pasos:

1. Accede a Google Cloud Platform y crea un proyecto nuevo o utiliza uno existente.
1. Habilita la API de Geocodificación en el proyecto.
1. Genera una clave de API para acceder a los servicios de Google Maps.
1. Crea un archivo llamado .env en el directorio raíz del proyecto.
1. Dentro del archivo .env, define la variable de entorno API_KEY con el valor de tu clave de API. Por ejemplo: API_KEY=Llave.

## Ejecución del archivo

Una vez que hayas instalado los módulos y configurado la clave de la API, puedes ejecutar el archivo Python:

```
python technicalTest3.py
```

El programa busca la dirección escrita y buscará el vecindario correspondiente. Además, implementa una función recursiva para incrementar el número de la dirección y verificar si el vecindario ha cambiado. Una vez haya cambiado el vecindario, la salida del programa muestra cuál es la nueva dirección y el nombre del nuevo barrio.
