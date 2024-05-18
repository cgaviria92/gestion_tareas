# Sistema de Gestión de Tareas

Este proyecto es un sistema simple para gestionar tareas, construido con Django y Django REST Framework. Permite crear, leer, actualizar y eliminar tareas. Cada tarea tiene un título, una descripción y un estado (pendiente, en progreso, completada).

## Requisitos

- Python 3.6 o superior
- Django 3.0 o superior
- Django REST Framework

## Instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/cgaviria92/gestion_tareas.git
    cd gestion_tareas
    ```

2. Crea un entorno virtual y actívalo:

    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa: env\Scripts\activate
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Realiza las migraciones de la base de datos siempre y cuando no este el archivo de sqlite:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. Crea un superusuario para acceder al panel de administración de Django cuando no este el archivo de sqlite:

    ```bash
    python manage.py createsuperuser
    ```

    Usa estas credenciales:
    - **Nombre de usuario**: admin
    - **Contraseña**: admin

6. Inicia el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

## Uso

### Acceso al Administrador de Django

Abre tu navegador y ve a `http://127.0.0.1:8000/admin`. Inicia sesión con las credenciales que creaste (admin/admin).

### API RESTful

Puedes interactuar con la API RESTful utilizando herramientas como Postman o CURL. Aquí tienes los endpoints disponibles:

- **Listar todas las tareas**: `GET /api/tareas/`
- **Crear una nueva tarea**: `POST /api/tareas/`
- **Obtener detalles de una tarea específica**: `GET /api/tareas/{id}/`
- **Actualizar una tarea**: `PUT /api/tareas/{id}/`
- **Eliminar una tarea**: `DELETE /api/tareas/{id}/`

## Ejemplos de Solicitudes con Postman

#### Proyecto3.postman_collection.json

## Documentación de la API

Puedes ver la documentación de la API en `http://127.0.0.1:8000/api/tareas/`.

## Pruebas

Pruebas unitarias:

```bash
python manage.py test
