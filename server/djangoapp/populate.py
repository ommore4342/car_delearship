"""Seed the database with initial CarMake and CarModel data."""
from .models import CarMake, CarModel


def initiate():
    car_data = [
        {
            'make': 'Toyota',
            'description': 'Japanese multinational automotive manufacturer',
            'country': 'Japan',
            'models': [
                ('Camry', 'SEDAN', 2023),
                ('RAV4', 'SUV', 2023),
                ('Corolla', 'SEDAN', 2022),
                ('Highlander', 'SUV', 2023),
                ('Tacoma', 'TRUCK', 2023),
            ],
        },
        {
            'make': 'Ford',
            'description': 'American multinational automobile manufacturer',
            'country': 'USA',
            'models': [
                ('Mustang', 'COUPE', 2023),
                ('F-150', 'TRUCK', 2023),
                ('Explorer', 'SUV', 2022),
                ('Escape', 'SUV', 2023),
                ('Bronco', 'SUV', 2023),
            ],
        },
        {
            'make': 'Chevrolet',
            'description': 'American automobile division of General Motors',
            'country': 'USA',
            'models': [
                ('Silverado', 'TRUCK', 2023),
                ('Equinox', 'SUV', 2023),
                ('Malibu', 'SEDAN', 2022),
                ('Traverse', 'SUV', 2023),
                ('Camaro', 'COUPE', 2023),
            ],
        },
        {
            'make': 'Honda',
            'description': 'Japanese public multinational conglomerate',
            'country': 'Japan',
            'models': [
                ('Civic', 'SEDAN', 2023),
                ('CR-V', 'SUV', 2023),
                ('Accord', 'SEDAN', 2022),
                ('Pilot', 'SUV', 2023),
                ('Ridgeline', 'TRUCK', 2023),
            ],
        },
        {
            'make': 'BMW',
            'description': 'German multinational corporate manufacturer of luxury vehicles',
            'country': 'Germany',
            'models': [
                ('3 Series', 'SEDAN', 2023),
                ('X5', 'SUV', 2023),
                ('5 Series', 'SEDAN', 2022),
                ('X3', 'SUV', 2023),
                ('M4', 'COUPE', 2023),
            ],
        },
        {
            'make': 'Mercedes-Benz',
            'description': 'German luxury and commercial vehicle automotive brand',
            'country': 'Germany',
            'models': [
                ('C-Class', 'SEDAN', 2023),
                ('GLE', 'SUV', 2023),
                ('E-Class', 'SEDAN', 2022),
                ('GLC', 'SUV', 2023),
                ('S-Class', 'SEDAN', 2023),
            ],
        },
    ]

    for entry in car_data:
        make, _ = CarMake.objects.get_or_create(
            name=entry['make'],
            defaults={
                'description': entry['description'],
                'country_of_origin': entry['country'],
            }
        )
        for model_name, car_type, year in entry['models']:
            CarModel.objects.get_or_create(
                car_make=make,
                name=model_name,
                defaults={'car_type': car_type, 'year': year},
            )

    print("Database seeded with car makes and models.")
