# Test Fullstack Aukko - Carlos Orostegui

## Descripción

La solución se compone de 4 proyectos, estos proyectos son:

* api
* data
* scraper
* web

### Proyecto API

Encargado de entregar las categorias y libros cargados por el servicio scraper.

### Proyecto DATA

Encargado la implementación de la libreria SQLAlchemy, contiene los modelos y el contexto principal.

### Proyecto SCRAPER

Encargado de obtener los datos desde la web http://books.toscrape.com, se compone principlamente de 2 servicios:

* BookScraper
* BookParser

El servicio BookScraper se encarga de leer el html correspondiente a los libros y categorias de la web, este servicio una vez finalizadas todas sus solicitudes guarda los datos en la carpeta data (categories.json y books.json).

El servicio BookParser se encarga de leer los datos recopilados por el servicio BookScraper y cargalos en BD, como caso practico cada vez que el servicio
BookParser es utilizado, se eliminan y se carga la metadata de la base de datos, este servicio solo cuenta con lógica de carga y no con lógica de actualización.

### Proyecto WEB

Encargado de visualizar los datos obtenidos desde el proyecto API.

##  Instrucciones

### Pre-requisitos

* Python 3.7
* Libreria Requests
* Libreria BeautifulSoup
* Libreria SQLAlchemy
* Libreria Flask-RESTful
* Libreria Flask-Cors

* NodeJS (v10.9.0) (version recomendada)

### Instalación

* pyp3
```
sudo apt-get install python3-pip
```
* Requests
```
pip3 install requests
```
* BeautifulSoup
```
pip3 install beautifulsoup4
```
* SQLAlchemy
```
pip3 install sqlalchemy
```
* Flask-RESTful
```
 pip3 install flask-restful
 pip3 install -U flask-cors
```

## Despliegue

* Para la ejecución del proyecto scraper se debe ejecutar el comando
```
 npm run scraper
```

* Para la ejecciòn del proyecto API se debe ejecutar el comando (terminal 1), el proyecto será ejectuado en localhost:3000
```
 npm run api
```

* Para la ejecciòn del proyecto WEB se deben ejecutar los siguientes comandos (terminal 2), el proyecto será ejecutado en localhost:8080
```
  cd web/
  npm install
  npm run dev
```
## Construido con

* Backend
    * Python 3.7
    * SQLAlchemy
    * BeautifulSoup
    * Requests
    * Flask-RESTful
* FrontEnd
    * VueJS
    * WebPack
    * ES6

## Autor

* **Carlos Orostegui** 
