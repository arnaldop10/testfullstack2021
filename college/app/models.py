from django.db import models


class Colegio(models.Model):
    nombre = models.CharField(max_length=150)
    direccion = models.CharField(max_length=250, null=True, blank=True)
    director = models.CharField(max_length=150, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.nombre}"


class Profesor(models.Model):
    rut = models.CharField(max_length=12)
    nombre_completo = models.CharField(max_length=150)
    correo = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self) -> str:
        return f"Rut: {self.rut}, Nombre: {self.nombre_completo}"


class Alumno(models.Model):
    rut = models.CharField(max_length=12)
    nombre_completo = models.CharField(max_length=150)
    correo = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) -> str:
        return f"Rut: {self.rut}, Nombre: {self.nombre_completo}"


class Curso(models.Model):
    colegio = models.ForeignKey(Colegio, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Profesor, null=True, on_delete=models.SET_NULL)
    alumnos = models.ManyToManyField(Alumno, related_name="alumno_curso")
    nombre = models.CharField(max_length=150)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.nombre}"


class Prueba(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    nota_maxima = models.IntegerField(default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.nombre}"


class Nota(models.Model):
    prueba = models.ForeignKey(Prueba, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    puntaje = models.IntegerField(default=0)

    def __str__(self) -> str:
        nombre_alumno = self.alumno.nombre_completo
        nombre_prueba = self.prueba.nombre

        return "Alumno: {}, Prueba: {}, Nota: {}".format(
            nombre_alumno, nombre_prueba, self.puntaje
        )

