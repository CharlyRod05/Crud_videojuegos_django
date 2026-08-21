from django.contrib import admin
from .models import Videojuego


@admin.register(Videojuego)
class VideojuegoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'plataforma', 'precio', 'fecha_lanzamiento')
    list_filter = ('genero', 'plataforma')
    search_fields = ('titulo',)
    ordering = ('titulo',)