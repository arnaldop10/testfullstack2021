from django.urls import path
from app.views import (
    ColegioListView,
    ColegioDetailView,
    ColegioCreateView,
    ColegioDeleteView,
    ColegioUpdateView,
)

app_name = 'app'

urlpatterns = [
    path('', ColegioListView.as_view(), name='colegio-list'),
    path('colegio/<int:pk>/detail', ColegioDetailView.as_view(),name='colegio-detail'),
    path('colegio/create/', ColegioCreateView.as_view(),name='colegio-create'),
    path('colegio/<int:pk>/update/', ColegioUpdateView.as_view(),name='colegio-update'),
    path('colegio/<int:pk>/delete/', ColegioDeleteView.as_view(),name='colegio-delete'),
]