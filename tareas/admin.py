from django.contrib import admin
from .models import Tarea

# Register your models here.

class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'estado', 'descripcion')
    list_filter = ('estado',)
    search_fields = ('titulo', 'descripcion')
    list_editable = ('estado',)
    ordering = ('estado',)  # Ordenar por estado

admin.site.register(Tarea, TareaAdmin)
