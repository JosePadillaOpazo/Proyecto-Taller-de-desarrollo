# imagen basada en Debian Bullseye
FROM debian:11.6

# Actualizar los paquetes del sistema
RUN apt-get update && apt-get upgrade -y

# Instalacion de herramientas necesarias
RUN apt-get install -y \
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

# Actualizacion de packages instalados
RUN apt-get update && apt-get upgrade -y

# Instalacion de wget
RUN apt-get install -y \
	wget

# ---------------------------- Descarga de Python 3.8.5, descomprimir y mover ---------------------------- 
RUN wget https://www.python.org/ftp/python/3.8.5/Python-3.8.5.tar.xz

RUN tar -xf Python-3.8.5.tar.xz

RUN mv Python-3.8.5 /usr/local/share/python3.8

# Configuracion y compilacion Python 3.8
RUN cd /usr/local/share/python3.8 && \
	 ./configure --enable-optimizations --enable-shared && \
	make altinstall && \
	ldconfig /usr/local/share/python3.8 

RUN cd / && rm Python-3.8.5.tar.xz

RUN python3.8 -m pip install --upgrade pip

# ---------------------------- Instalacion Kivy ----------------------------

RUN python3.8 -m pip install "kivy[base]" kivy_examples 

RUN python3.8 -m pip install kivymd

# ---------------------------- Instalacion libreria openpyxl (Para el manejo de archivos xlsx con python)  ----------------------------
RUN python3.8 -m pip install openpyxl

# Establece el directorio de trabajo y copia archivos al contenedor
WORKDIR /app

COPY . /app

# Muestra las instalaciones de pip, lanza el programa prueba.py y deja abierta la consola
CMD sh -c "python3.8 -m pip list && python3.8 prueba.py && bash"
