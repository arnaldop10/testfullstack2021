from django.contrib import admin
from .models import Colegio, Alumno, Profesor, Curso, Nota, Prueba


admin.site.register(Colegio)

admin.site.register(Alumno)

admin.site.register(Profesor)

admin.site.register(Curso)

admin.site.register(Nota)

admin.site.register(Prueba)
