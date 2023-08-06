# Guía de Contribución

## Equipo de Desarrollo

## Autores

- [José Padilla](@JosePadillaOpazo) - ~~Dueño del proyecto~~ - jospadil@alumnos.ubiobio.cl

## Estándar de Codificación

### Estilo de Codificación

El estilo de código de este proyecto debe seguir las recomendaciones de los estándares:
- ~~[PEP 8](https://peps.python.org/pep-0008/)~~


### Configuraciones para editores de código

Antes de escribir tu código, verifica que las configuraciones generales de tu editor estén ajustados de la siguiente manera:

- Final/Salto de Línea (EOL - End of Line ) = LF,CRLF
- Codificación de Archivos de Código (Encoding - Charset) = UTF-8, ISO-8859-1
- Usa 4 (cuatro) espacios por indentación.
- Utilizar la nomenclatura de snake case para nombrar variables

### Editor Config

Busca e instala [Editor Config](https://editorconfig.org/), como plugin para tu IDE o Editor de Código, y de esta forma, automáticamente se configurarán las opciones para editores de código mencionadas anteriormente.

## Desarrollo del código

### Arquitectura del Sistema - Patrones de Diseño

- ~~El proyecto se compone de: Codigo en lenguaje python y codigo en lenguaje kivy y kivyMD~~

## Interacción con el repositorio

1. Crear una nueva rama en la que desea trabajar a partir de la rama master

2. Desarrollar el código en la nueva rama creada
    - Realizar los commit's en la rama creada
    - Mencionar en el mensaje del commit el lo que se desarrollo.

3. Construir los test unitarios y de integración que comprueben el funcionamiento de tu desarrollo, y evitar que por accidente tu nuevo código pueda romper el resto de funcionalidades del sistema

4. Enviar tu código al repositorio, solo cuando los test estén en verde, y abrir un Merge Request
    - Describir que cosas se integrarán a la rama master
    - Describir los criterios de aceptación y revisión del código y los cambios

5. Esperar la aprobación por parte de [José Padilla](@JosePadillaOpazo) dueño de este repositorio para la integración de tú código a la rama master


### Archivos/Directorios que no deben ser versionados o enviados al repositorio (**no** incluir en los **commit's**)

- `config/*`
- `vendor/*`
- `env/*` (En caso de utilizar algun environment de desarrollo)

### Archivos/Directorios que no deben estar en ambientes de producción

- `Docker/*`
- `env/*` (En caso de utilizar algun environment de desarrollo)
- `README.md`
- `.gitignore`
- `.git/*`

