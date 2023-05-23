## Instalación

Ejecutar en un cmd en el directorio donde tenemos la carpeta del proyecto descomprimida:

```sh
code .
```

Utilizar python version 3.10.6


Una vez que tenemos el Visual Studio Code cont todas las carpetas del proyecto abiertas, 
Abrimos un terminal dentro de Visual Studio Code y ejecutamos el siguiente comando:

```sh
pip install -r requirements.txt
```
## Ejecución  

Dentro del terminal de VSC:

```sh
python.exe -m uvicorn app:app --reload
```

