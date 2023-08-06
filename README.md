"Aplicación móvil de apoyo a CITEC UBB para el proceso de inspección de edificaciones"

El equipo del Centro de Investigación de Tecnologías de la Construcción CITEC actulamente realiza inspecciones de viviendas y construcciones, 
las cuales se realizan con papel y lapiz, el siguiente proyecto busca digitalizar todo el proceso de obtencion de informacion para asi disminuir el trabajo y optimizar los tiempos del proceso. 
En esta primera etapa del proyecto, se busca obtener la informacion y recopilarla en un archivo .xlsx el cual se guardara con el nombre que ingrese el ususario. 
Los ususarios seran los inspectores del equipo CITEC, quienes son los encargados de realizar las inspecciones en terreno y luego realizan un resumen de la informacion adquirida. 
La aplicacion actualmente esta construida con el lenguaje Python y con modulos que cuenta este mismo, tales como Kivy, KivyMD para la parte grafica de la aplicacion y Openpyxl para el manejo de archivos .xlsx.

## Software stack

La Aplicacion Movil de apoyo a CITEC que corre sobre el siguiente software:

- ~~Debian GNU/Linux 11.6 Bullseye~~
- ~~Python 3.8.5~~
- ~~Kivy 2.2.1~~
- ~~KivyMD 1.1.1~~
- ~~Openpyxl~~
- **IMPORTANTE**: Por razones de compatibilidad con la parte grafica del proyecto, no fue posible ejecutarlo en la distribucion mencionada.

## Configuraciones de Ejecución para Entorno de Desarrollo/Produccción

-**IMPORTANTE**: Debe tener instalados los interpretes de lenguaje y sus dependencias antes de ejecutar localmente.

-Cree una carpeta con el nombre que desee (Ejemplo git_JP)

-Dentro de la carpeta habra una consola y utilice el comando 
```bash
git clone https://github.com/JosePadillaOpazo/Proyecto-Taller-de-desarrollo.git
```

-Mediante la consola acceda a la carptea obtenida con el git clone (Ej:  cd .\Proyecto-Taller-de-desarrollo\)

-Para lanzar el programa y probarlo, debe escribir en la consola el comando de python junto al nombre del archivo a ejecutar. (Ej:python3 main.py)

-para revisar el contenido de los archivos main.py y main.kv debe abrirlos con el editor de texto de su preferencia. (Ej: nano main.py)

### Credenciales de Base de Datos y variables de ambiente

-Este proyecto no cuenta con coneccion a base de datos.

### ~~Docker, Máquina Virtual, Sistema Operativo~~

-Con una terminal situarse dentro del directorio raiz donde fue clonado este repositorio, por ej: `~/git_JP/Proyecto-Taller-de-desarrollo/`.

-Una vez situado en la raiz del proyecto, dirigirse al directorio `docker` y ejecutar lo siguiente para construir la imagen docker:

```bash
docker build -t mi-proyecto .
```

-Una vez creada la imagen, la puede revisar utilizando el siguiente comando:
```bash
docker images
```
-Una vez construida la imagen, lanzar un contenedor montando un volumen que contenga el código de prueba que esta junto al archivo dockerfile.

```bash
docker run -ti mi-proyecto
```

-Una vez lanzado el contenedor le mostrara el listado de packages instalados y se ejecutara el archivo prueba.py, el cual contiene un mensaje que se mostrara por consola. 

-Finalmente quedara la bash abierta para poder seguir utilizando el contenedor. Si lo desea puede ejecutar el siguiente comando en la bash del contenedor: 

```bash
python3.8 main.py
```

-Luego de lanzar el comando, se mostrara el intento de ejecucion del archivo main.py que cuenta con un "hello world" de ejemplo de la libreria KivyMD, el cual mostrara que no tiene compatibilidad con la version de linux utilizada.

-Para salir de la ejecucion del contenedor excriba en la consola de este el comando "exit".

-Para elminar el contenedor: 
-Una vez cerrado el contenedor utilice el comando:

```bash
docker ps -a
```
-Copie el ID del container que se estaba utilizando.

-Utilice el comando:
```bash
docker rm "ID del comando"
```
-Para eliminar la imagen:(no debe haber contenedores creados a partir de la imagen a brorar)
-Utilice el comando:
```bash
docker images
```

-Copie el nombre del la imagen a borrar del listado de Repository mostrado por el comando.

-Utilice el comando:
```bash
docker rmi "Nombre de la imagen"
```

### Instalar dependencias del proyecto

-Cambiar a super usuario:
```bash
sudo su
```
-Ingrese la contraseña de super ususario.

-Actualizar los paquetes del sistema:
```bash
apt-get update && apt-get upgrade -y
```

-Instalar las dependencias necesarias 
```bash
apt-get install -y \
	build-essential \
	zlib1g-dev \
	libncurses5-dev \
	libgdbm-dev \
	libnss3-dev \
	libssl-dev \
	libsqlite3-dev \
	libreadline-dev \
	libffi-dev \
	curl \
	libbz2-dev 
```
-Actualizar los paquetes instalados:
```bash
apt-get update && apt-get upgrade -y
```
-Instalar wget
```bash
apt-get install -y \
	wget
```

Instalacion de Python
-Descargar Python 3.8.5
```bash
wget https://www.python.org/ftp/python/3.8.5/Python-3.8.5.tar.xz
```

-Descomprimir archivo
```bash
tar -xf Python-3.8.5.tar.xz
```

-Mover archivos a directorio /usr/local/share/python3.8:
```bash
mv Python-3.8.5 /usr/local/share/python3.8
```

-Comfiguracion de Python:
```bash
cd /usr/local/share/python3.8 && \
	 ./configure --enable-optimizations --enable-shared && \
	make altinstall && \
	ldconfig /usr/local/share/python3.8 
```

-Actualizacion de pip
```bash
python3.8 -m pip install --upgrade pip
```

Instalacio de Kivy:
```bash
python3.8 -m pip install "kivy[base]" kivy_examples 
```

Instalacio de KivyMD:
```bash
python3.8 -m pip install kivymd
```

Instalacio de Openpyxl:
```bash
python3.8 -m pip install openpyxl
```
Esas son las dependencias necesarias para ejecutar el proyecto. 

## Construido con

- ~~[Python](https://www.python.org/downloads/release/python-385/) - Lenguaje de programacion utilizado~~
- ~~[Kivy](https://kivy.org/doc/stable/) - Modulo de Python utilizado para la parte grafica~~
- ~~[KivyMD](https://kivymd.readthedocs.io/en/1.1.1/) - Modulo de Python utilizado para la parte grafica~~
- ~~[Openpyxl](https://openpyxl.readthedocs.io/en/stable/) - Utilizado en el manejo de archivos .xlsx~~
- ~~[Pip](https://pypi.org/project/pip/) -Utilizado en el manejo de dependencias~~


## Licencia

Este proyecto fue construido con la licencia AAA, - ver [LICENSE.md](LICENSE.md) para mayor información


## Contribuir al Proyecto

- Por favor lea las instrucciones para contribuir al proyecto en [CONTRIBUTING.md](CONTRIBUTING.md)

## Agradecimientos
