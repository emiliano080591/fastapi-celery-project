# Proyecto de fastApi con celery

### Levantar celery
```shell
celery -A main.celery worker --loglevel=info
```
### Correr celery con monitoreo de flower
```shell
celery -A main.celery flower --port=5555
```

### Iniciar alembic
```shell
alembic init alembic
```

### Hacer migración
```shell
alembic revision --autogenerate
alembic upgrade head
```