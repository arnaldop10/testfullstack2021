**Modelo de Datos**

![Modelo ER](https://github.com/arnaldop10/testfullstack2021/blob/main/modelo_entidad.png)


**SQL**
1. Consulta de alumnos para curso 'programación'

```sql
Select rut, nombre_completo, email
from Alumno
inner join AlumnoCurso 
on (id=alumno_id)
where curso_id in (select curso_id from Curso where nombre = 'programación')
order by rut, nombre_completo;
```

2.
