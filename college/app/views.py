from typing import List
from django.http import HttpResponse
from django.views.generic import (
    DetailView, CreateView, UpdateView, DeleteView, View
)
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .models import Colegio, Alumno, Profesor, Curso, Nota, Prueba


############################# COLEGIOS #######################################

class ColegioView(View):
    model = Colegio
    fields = '__all__'
    success_url = reverse_lazy('app:colegio-list')


class ColegioListView(ColegioView, ListView):
    """Listar los colegios registrados"""
    template_name = "app/colegio/colegio_list.html"


class ColegioDetailView(ColegioView, DetailView):
    """Clase para la vista del detalle del colegio"""
    template_name = "app/colegio/colegio_detail.html"


class ColegioCreateView(ColegioView, CreateView):
    """Clase para crear un colegio"""
    template_name = "app/colegio/colegio_form.html"


class ColegioUpdateView(ColegioView, UpdateView):
    """Actualizar los colegios registrados"""
    template_name = "app/colegio/colegio_form.html"


class ColegioDeleteView(ColegioView, DeleteView):
    """Eliminar los colegios registrados"""
    template_name = "app/colegio/colegio_confirm_delete.html"
