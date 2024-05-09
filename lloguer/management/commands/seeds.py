# lloguer/management/commands/seed_automobils.py

from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from ...models import Automobil

class Command(BaseCommand):
    help = 'Seeds the Automobil model with dummy data'

    def add_arguments(self, parser):
        parser.add_argument('num_automobils', nargs='?', type=int, default=200, help='Number of automobils to create (default: 200)')

    def handle(self, *args, **options):
        num_automobils = options['num_automobils']
        faker = Faker()
        marcas = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Volkswagen']
        modelos = ['Corolla', 'Civic', 'Focus', 'Cruze', 'Jetta']

        for _ in range(num_automobils):
            marca = faker.random.choice(marcas)
            model = faker.random.choice(modelos)
            matricula = faker.unique.bothify(text='??###??')
            Automobil.objects.create(marca=marca, model=model, matricula=matricula)

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {num_automobils} automobils.'))