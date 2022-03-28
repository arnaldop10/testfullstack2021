**Modelo de Datos**

![Modelo ER](https://github.com/arnaldop10/testfullstack2021/blob/main/modelo_colegio.png)


**SQL**
1. Consulta de alumnos para curso 'programación'

```sql
Select rut, nombre_completo, email
from Alumno a
inner join AlumnoCurso ac
on (a.id=ca.alumno_id)
where curso_id in (select id from Curso where nombre = 'programación')
order by rut, nombre_completo;
```

2. Escriba una Query que calcule el promedio de notas de un alumno en un curso.

```sql
Select avg(puntaje_prueba) as promedio
from Nota as n
inner join Alumno as a
on (n.alumno_id=a.id)
inner join Prueba as p
on (n.prueba_id=p.id)
inner join Curso as c
on (p.curso_id=c.id)
where a.rut=? and c.nombre=?;
```

3. Escriba una Query que entregue a los alumnos y el promedio que tiene en cada curso.

```sql
Select a.rut, a.nombre_completo, a.email, c.nombre, avg(n.puntaje_prueba) as promedio
from Alumno as a
inner join AlumnoCurso as ac
on (a.id=ac.alumno_id)
inner join Curso as c
on (ac.curso_id=c.id)
inner join Prueba as p
on (p.curso_id=c.id)
inner join Nota as n
on (n.prueba_id=p.id and n.alumno_id=a.id)
group by a.rut, a.nombre_completo, a.email, c.nombre;
order by a.rut, a.nombre_completo, a.email, c.nombre;
```

4. Escriba una Query que lista a todos los alumnos con más de un curso con promedio rojo.

```sql
Select a.rut, a.nombre_completo, a.correo, c.nombre, avg(n.puntaje) as promedio
from Alumno as a
inner join AlumnoCurso as ac
on (a.id=ac.alumno_id)
inner join Curso as c
on (ac.curso_id=c.id)
inner join Prueba as p
on (p.curso_id=c.id)
inner join Nota as n
on (n.prueba_id=p.id and n.alumno_id=a.id)
group by a.rut, a.nombre_completo, a.correo, c.nombre
having avg(n.puntaje) < 5
order by a.rut, a.nombre_completo, a.correo, c.nombre;
```

5. La respuesta es la opción b) 190