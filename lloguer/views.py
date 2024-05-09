from django.shortcuts import render
from .models import Automobil

def vehicle_list(request):
    vehicles = Automobil.objects.all()
    return render(request, 'vehicle_list.html', {'vehicles': vehicles})