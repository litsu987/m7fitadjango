from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Automobil(models.Model):
    marca = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    matricula = models.CharField(max_length=10)
    def __str__(self):
        return self.matricula + ' - ' + self.marca + " " + self.model


class Reserva(models.Model):
    automovil = models.ForeignKey(Automobil, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField(default=timezone.now)
    fecha_fin = models.DateTimeField()
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} reservó {self.automovil.marca} {self.automovil.model} desde {self.fecha_inicio} hasta {self.fecha_fin}"
