# Proyecto de fastApi con celery

### Levantar ambiente con docker-compose

```shell
docker-compose build
docker-compose up -d
```

### Ver logs de docker-compose

```shell
docker-compose logs -f
```

### Entrar a la terminal de alguno de los servicios de docker-compose

```shell
docker-compose exec <service-name> bash
# for example:
# docker-compose exec web bash
```

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