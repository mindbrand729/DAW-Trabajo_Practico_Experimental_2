# DAW-Trabajo_Practico_Experimental_2
Instrucciones para la ejecución y el correcto funcionamiento del repositorio

Requisitos previos

Antes de ejecutar el proyecto, asegúrese de tener lo siguiente instalado:

    Python 3.9 o superior (recomendado: Python 3.11)
    pip (gestor de paquetes de Python)
    Opcional: Visual Studio Code o cualquier editor de texto
    Git (si va a clonar el repositorio directamente desde GitHub)

# Cómo Obtener el Proyecto
Opción 1: Desde Google Drive:

Descargue y descomprima la carpeta DAW-Trabajo_Practico_Experimental_1... en su computadora.

Opción 2: Desde GitHub (Archivo ZIP):

Ingrese al repositorio:

Haga clic en Code → Download ZIP.

Descomprima la carpeta del proyecto.

Opción 3: Clonación con Git (recomendado):

En Windows abre la terminal (PowerShell, CMD o terminal de VS Code) y ejecute:

    git clone https://github.com/mindbrand729/DAW-Trabajo_Practico_Experimental_2.git

# Entrar el la carpeta
Una vez creada la carpeta, ejecuta:

    cd .\DAW-Trabajo_Practico_Experimental_2

# Crear y activar el entorno virtual
Crear el entorno virtual

    python -m venv venv

Activar entorno virtual:

En Windows:

    venv\Scripts\activate
    
En Mac/Linux:

    source venv/bin/activate

Problemas comunes en Windows (PowerShell)

Si aparece un error como:

    File ...\Activate.ps1 cannot be loaded because running scripts is disabled...

Windows PowerShell está bloqueando la ejecución de scripts. Soluciones:

Opción 1: Activar usando cmd.exe

En lugar de usar PowerShell, abre una ventana de comandos normal (cmd) e intenta activar el entorno:

    venv\Scripts\activate

Opción 2: Cambiar la política de PowerShell (temporal o permanente)

Temporal (sólo para esta sesión):
    
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
    venv\Scripts\activate

Permanente (menos recomendable en equipos institucionales):

    Set-ExecutionPolicy RemoteSigned
    venv\Scripts\activate

# Instalar dependencias
Una vez activado el entorno virtual, ejecuta:
    
    pip install -r requirements.txt

# Configurar la base de datos PostgreSQL
Antes de ejecutar el proyecto:

1.	Instalar PostgreSQL si no lo tienen.

2.	Crear una base de datos con los mismos datos:

        Nombre: practicatpe2
        Usuario: practicausr25
        Contraseña: practic35
        Host: localhost
        Puerto: 5432

    Crearla desde SQL Shell (psql):

        CREATE DATABASE practicatpe2;
        CREATE USER practicausr25;
        \c practicatpe2
        ALTER ROLE practicausr25 WITH PASSWORD 'practic35';
        GRANT ALL ON SCHEMA public TO practicausr25;

# Verificar que el settings.py tenga los datos correctos
En settings.py, la configuración de base de datos debe verse así:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'practicatpe2',
            'USER': 'practicausr25',
            'PASSWORD': 'practic35',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

# Realizar migraciones y levantar el servidor
Después de tener todo listo:

    python .\Floristeria\manage.py makemigrations
    python .\Floristeria\manage.py migrate
    python .\Floristeria\manage.py runserver

O en una sola linea:

    python .\Floristeria\manage.py makemigrations; python .\Floristeria\manage.py migrate; python .\Floristeria\manage.py runserver


