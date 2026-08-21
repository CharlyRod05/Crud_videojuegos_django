from django.urls import path
from . import views

app_name = 'videojuegos'

urlpatterns = [
    path('', views.lista_videojuegos, name='lista'),
    path('crear/', views.crear_videojuego, name='crear'),
    path('editar/<int:pk>/', views.editar_videojuego, name='editar'),
    path('eliminar/<int:pk>/', views.eliminar_videojuego, name='eliminar'),
]