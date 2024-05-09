from django.contrib import admin
from .models import Automobil, Reserva
admin.site.register(Automobil)

class AutomobilAdmin(admin.ModelAdmin):
    list_display = ('matricula', 'marca', 'model')
    search_fields = ('matricula', 'marca', 'model')
    list_filter = ('marca', 'model')

class ReservaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'automovil', 'fecha_inicio', 'fecha_fin', 'creado_en')
    list_filter = ('usuario', 'automovil', 'fecha_inicio', 'fecha_fin')
    search_fields = ('usuario__username', 'automovil__marca', 'automovil__model')
    date_hierarchy = 'creado_en'
    ordering = ('-creado_en',)

# Registrar el modelo Reserva en el panel de administración utilizando la clase de administración personalizada
admin.site.register(Reserva, ReservaAdmin)
