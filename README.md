# Base de datos FabLab USM

## Entorno de desarrollo

Instalar el controlador de dependencias Poetry:

```
python3 -m pip install poetry
```

Luego crear el entorno virtual e instalar:

```
poetry install
poetry shell
```

Para correr el servicio, primero crear la base de datos migrando, creando el
superusuario del sistema y corriendo el servidor de prueba

```
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```

Luego el api se puede ver en http://127.0.0.1:8000/api/

## FAQ

**¿Qué base de datos ocupa?**

Está programado para ser agnóstico a la base de datos, pero como prueba, se
han usado algunos módulos de PostgreSQL. El entorno de desarrollo está
*hardcodeado* para funcionar con SQLite, ignorando los campos exclusivos para
psql, pero debería ser suficiente y rápido para terminar el desarrollo y
llevarlo a producción

**¿Dónde puedo encontrar la documentación de cada módulo?**

El código está comentado para esos efectos. No se ha usado ningún generador de
documentación como Sphinx pero siéntase libre de implementarlo.