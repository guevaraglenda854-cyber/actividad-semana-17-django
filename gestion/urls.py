from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("duenos/nuevo/", views.crear_dueno, name="crear_dueno"),
    path("duenos/<int:pk>/editar/", views.editar_dueno, name="editar_dueno"),
    path("duenos/<int:pk>/eliminar/", views.eliminar_dueno, name="eliminar_dueno"),
    path("mascotas/nueva/", views.crear_mascota, name="crear_mascota"),
    path("mascotas/<int:pk>/editar/", views.editar_mascota, name="editar_mascota"),
    path("mascotas/<int:pk>/eliminar/", views.eliminar_mascota, name="eliminar_mascota"),
    path("consultas/nueva/", views.crear_consulta, name="crear_consulta"),
    path("consultas/<int:pk>/editar/", views.editar_consulta, name="editar_consulta"),
    path("consultas/<int:pk>/eliminar/", views.eliminar_consulta, name="eliminar_consulta"),
]