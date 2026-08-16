"""
Management command: python manage.py seed_data
Seeds CarMake, CarModel, Dealer, Review data and creates a default admin user.
"""
import os
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Seed the database with initial dealers, reviews, car data, and admin user'

    def handle(self, *args, **options):
        from djangoapp.populate import initiate, seed_dealers

        self.stdout.write('Seeding car makes and models...')
        initiate()
        self.stdout.write(self.style.SUCCESS('  Car data seeded.'))

        self.stdout.write('Seeding dealers and reviews...')
        seed_dealers()
        self.stdout.write(self.style.SUCCESS('  Dealer/review data seeded.'))

        # Create default admin user if it doesn't exist
        admin_user = os.environ.get('ADMIN_USER', 'admin')
        admin_pass = os.environ.get('ADMIN_PASS', 'Admin1234!')
        admin_email = os.environ.get('ADMIN_EMAIL', 'admin@carsdealership.com')

        if not User.objects.filter(username=admin_user).exists():
            User.objects.create_superuser(
                username=admin_user,
                email=admin_email,
                password=admin_pass,
            )
            self.stdout.write(self.style.SUCCESS(f'  Superuser "{admin_user}" created.'))
        else:
            self.stdout.write(f'  Superuser "{admin_user}" already exists.')

        self.stdout.write(self.style.SUCCESS('Seeding complete!'))
