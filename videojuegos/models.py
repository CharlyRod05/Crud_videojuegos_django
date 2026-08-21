from django.db import models

class Videojuego(models.Model):
    titulo = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    plataforma = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_lanzamiento = models.DateField()