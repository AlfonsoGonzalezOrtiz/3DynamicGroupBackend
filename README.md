# Construcción de objetos 3D mediante módulos predefinidos

# Introducción
En la actualidad, existen distintos softwares específicos para la representación de objetos en 3D como 
(Autocad, 3DStudio, Maya, Blender, etc.) que permiten componer de forma "sencilla" objetos. El problema
viene dado, porque no son sencillos de usar para el usuario inexperto, requiriendo mucho dominio de este 
tipo de software. El funcionamiento de este tipo de herramientas resulta demasiado complicado para hacer 
lo que quieren, y, sobre todo, cuando no existe suficiente tiempo para dedicar en aprender una nueva 
tecnología, ni tan siquiera motivación para hacerlo, por lo que sería de gran utilidad un recurso listo para 
usar que no supusiese un gran coste de tiempo y esfuerzos en aprender la herramienta.
 Por ello, surge la necesidad de crear una aplicación web que permita realizar esta tarea cómodamente
para usuarios sin formación, modificando, además, los módulos para que integren elementos de atracción
que hagan más fácil su anclaje, con una colección de módulos predefinidos que permita a nuestra aplicación 
ser más accesible para mayor parte de la población.
 Con el nacimiento de WebGL (Web Graphics Language), surge la posibilidad de poder trabajar con 
escenas gráficas y objetos 3D en navegadores web. Esta tecnología permite al usuario la utilización del 
software sin necesidad de instalar ningún programa o aplicación en sus dispositivos personales y sin 
necesidad de configuración, disminuyendo así la carga de memoria que supondría almacenar los archivos 
de los programas

Esta aplicación web puede resultar de mucha utilidad en muchos campos, tales como: la arquitectura,
para mostrar la elaboración de una construcción a gran escala, el diseño de interiores, pudiendo realizar un 
modelo 3D capaz de simular la decoración de una habitación y el diseño industrial, permitiendo crear 
maquinarias complejas a partir de módulos más simples.
Una de las principales ventajas de esta plataforma es que se podrán distribuir los modelos realizados en 
el formato estándar GLTF basado en JSON, el cual permitirá comprimir y transferir de forma eficiente los 
diseños 3D entre aplicaciones, minimizando el procesamiento en tiempo de ejecución en aplicaciones que 
usan WebGL y otras APIs(Interfaz de programación para aplicaciones).


# Objetivos
Con este TFG se pretende desarrollar una aplicación web con un visor 3D, que permita la construcción 
de objetos complejos a partir de otros objetos más simples, incluyendo elementos de atracción que faciliten 
su anclaje.
Los principales objetivos son:
• La plataforma debe ser accesible desde cualquier dispositivo moderno.
• La arquitectura de la aplicación estará segmentada por una interfaz de usuario “front-end”, un 
sistema de gestión de la información “back-end” y un servidor de bases de datos. 
• Permitir la exportación de los diseños 3D en formato estándar GLTF.
• El visor 3D permitirá navegar por el espacio pudiendo ampliar y reducir la vista, así como, el 
cambio de perspectiva.
• Definir un mecanismo óptimo para la atracción y anclaje entre módulos u objetos simples.
• Incluir las funcionalidades de coger, soltar y rotar para los objetos del espacio. 
• Disponer de módulos predefinidos que se podrán seleccionar para facilitar la creación de objetos.
 El objetivo de esta aplicación es que sea minimalista con las funcionalidades necesarias para llevar a 
cabo nuestra principal tarea, de tal modo que, un usuario sin formación sea capaz de realizarla sin mucho 
dominio de nuestra aplicación e incluso de otras aplicaciones. Con lo cual, la existencia de módulos 
predefinidos, un mecanismo óptimo de anclaje de objetos y el hecho de que sea accesible desde cualquier 
navegador moderno simplificaría cuantiosamente la tarea al usuario inexperto. Esto permitiría que nuestra 
aplicación sea más accesible para mayor parte de la población que no poseen muchos conocimientos tanto 
de informática como de diseño 3D en específico.

# Estructura de la aplicación

La estructura de nuestro backend está formada por los siguientes elementos:

- Una carpeta "pycache" que almacena archivos en caché generados por el intérprete de Python.
- Una carpeta "config" que contiene archivos de configuración para el proyecto.
- Una carpeta "models" que contiene los modelos de datos utilizados en el proyecto.
- Una carpeta "routes" que contiene los archivos de enrutamiento y controladores del proyecto.
- Un archivo ".gitignore" que especifica los archivos y directorios que deben ser ignorados por el control de versiones Git.
- Un archivo ".gitattributes" que permite configurar atributos específicos de Git para ciertos archivos o directorios.
- Un archivo "app.py" que contiene el código principal de la aplicación.
- Un archivo "db.json" que proporciona una copia de los datos de la base de datos en formato JSON utilizada por la aplicación.
- Un archivo "requirements.txt" que enumera las dependencias del proyecto para su instalación.
- Un archivo "Dockerfile" que contiene las instrucciones para construir una imagen de Docker para el proyecto.
- Un archivo "Readme.md" que proporciona documentación e instrucciones sobre el proyecto para los colaboradores y usuarios.

# Guía de instalación

## BACKEND

### REQUISITOS

- Tener instalado Python v3.10.6 o una versión superior. Puedes descargarlo desde aquí.
- Tener Docker instalado para los pasos alternativos. Puedes obtenerlo desde este enlace.

### Pasos de instalación

Opción 1:

1. Abrir un terminal de comandos.
2. Acceder a la carpeta raíz del proyecto.
3. Ejecutar el comando 'pip install -r requirements.txt'.
4. Ejecutar el comando 'python.exe -m uvicorn app:app --reload'.
5. La aplicación debería estar lista para poder visualizarse en su navegador con 'localhost:8000'.

Opción 2 | Docker:

1. Abrir un terminal de comandos.
2. Acceder a la carpeta raíz del proyecto.
3. Ejecutar el comando 'pip install -r requirements.txt'.
4. Tener cargado el motor de Docker, 'Docker Desktop' en Windows o 'Docker Engine' en Linux.
5. Crear un contenedor con el siguiente comando 'docker build -t <nombreImagen> .'.
6. Ejecutar el contenedor con 'docker run -p 8000:8000 <nombreImagen>'.
7. La aplicación debería estar lista para poder visualizarse en su navegador con 'localhost:8000'.