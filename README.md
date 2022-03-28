# testfullstack2021

## Prueba realizada para la empresa Capitaria

Para su instalación se deben crear los contenedores de docker usando:

```
docker-compose build
docker-compose up
```

Para cargar la información inicial, aplicar los fixtures generados:

```
docker-compose up
docker exec -it college_web_1 bash 
python manage.py loaddata colegio.yaml
python manage.py loaddata profesor.yaml
python manage.py loaddata alumno.yaml
python manage.py loaddata curso.yaml
python manage.py loaddata prueba.yaml
python manage.py loaddata nota.yaml
```

Abrir en el navegador el siguiente link: [App](https://localhost:8000)
