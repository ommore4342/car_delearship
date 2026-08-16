"""Seed the database with initial data for all models."""
from .models import CarMake, CarModel, Dealer, Review


def initiate():
    """Seed CarMake and CarModel data."""
    car_data = [
        {'make': 'Toyota',        'description': 'Japanese multinational automotive manufacturer',       'country': 'Japan',   'models': [('Camry','SEDAN',2023),('RAV4','SUV',2023),('Corolla','SEDAN',2022),('Highlander','SUV',2023),('Tacoma','TRUCK',2023)]},
        {'make': 'Ford',          'description': 'American multinational automobile manufacturer',       'country': 'USA',     'models': [('Mustang','COUPE',2023),('F-150','TRUCK',2023),('Explorer','SUV',2022),('Escape','SUV',2023),('Bronco','SUV',2023)]},
        {'make': 'Chevrolet',     'description': 'American automobile division of General Motors',      'country': 'USA',     'models': [('Silverado','TRUCK',2023),('Equinox','SUV',2023),('Malibu','SEDAN',2022),('Traverse','SUV',2023),('Camaro','COUPE',2023)]},
        {'make': 'Honda',         'description': 'Japanese public multinational conglomerate',          'country': 'Japan',   'models': [('Civic','SEDAN',2023),('CR-V','SUV',2023),('Accord','SEDAN',2022),('Pilot','SUV',2023),('Ridgeline','TRUCK',2023)]},
        {'make': 'BMW',           'description': 'German multinational luxury vehicles manufacturer',   'country': 'Germany', 'models': [('3 Series','SEDAN',2023),('X5','SUV',2023),('5 Series','SEDAN',2022),('X3','SUV',2023),('M4','COUPE',2023)]},
        {'make': 'Mercedes-Benz', 'description': 'German luxury and commercial vehicle automotive brand','country': 'Germany', 'models': [('C-Class','SEDAN',2023),('GLE','SUV',2023),('E-Class','SEDAN',2022),('GLC','SUV',2023),('S-Class','SEDAN',2023)]},
    ]
    for entry in car_data:
        make, _ = CarMake.objects.get_or_create(
            name=entry['make'],
            defaults={'description': entry['description'], 'country_of_origin': entry['country']}
        )
        for model_name, car_type, year in entry['models']:
            CarModel.objects.get_or_create(car_make=make, name=model_name, defaults={'car_type': car_type, 'year': year})


def seed_dealers():
    """Seed Dealer and Review data into SQLite."""
    if Dealer.objects.count() > 0:
        return  # already seeded

    dealers_data = [
        {'city': 'Wichita',       'state': 'Kansas',        'zip': '67201', 'address': '100 Auto Blvd',       'full_name': 'Wichita Motors',        'phone': '316-555-0101'},
        {'city': 'Overland Park', 'state': 'Kansas',        'zip': '66213', 'address': '200 Car Lane',        'full_name': 'Overland Park Autos',   'phone': '913-555-0102'},
        {'city': 'Chicago',       'state': 'Illinois',      'zip': '60601', 'address': '300 Lake Shore Dr',   'full_name': 'Chicago Premium Cars',  'phone': '312-555-0103'},
        {'city': 'Houston',       'state': 'Texas',         'zip': '77001', 'address': '400 Main St',         'full_name': 'Houston Auto Center',   'phone': '713-555-0104'},
        {'city': 'Phoenix',       'state': 'Arizona',       'zip': '85001', 'address': '500 Desert Rd',       'full_name': 'Phoenix Dealership',    'phone': '602-555-0105'},
        {'city': 'Los Angeles',   'state': 'California',    'zip': '90001', 'address': '600 Sunset Blvd',     'full_name': 'LA Luxury Motors',      'phone': '213-555-0106'},
        {'city': 'New York',      'state': 'New York',      'zip': '10001', 'address': '700 5th Avenue',      'full_name': 'NYC Auto Group',        'phone': '212-555-0107'},
        {'city': 'Miami',         'state': 'Florida',       'zip': '33101', 'address': '800 Ocean Drive',     'full_name': 'Miami Car Expo',        'phone': '305-555-0108'},
        {'city': 'Seattle',       'state': 'Washington',    'zip': '98101', 'address': '900 Pike St',         'full_name': 'Seattle Motors',        'phone': '206-555-0109'},
        {'city': 'Denver',        'state': 'Colorado',      'zip': '80201', 'address': '1000 Mile High Ave',  'full_name': 'Denver Dealer Network', 'phone': '720-555-0110'},
        {'city': 'Topeka',        'state': 'Kansas',        'zip': '66601', 'address': '1100 Capital Ave',    'full_name': 'Topeka Auto World',     'phone': '785-555-0111'},
        {'city': 'Boston',        'state': 'Massachusetts', 'zip': '02101', 'address': '1200 Boylston St',    'full_name': 'Boston Premier Motors', 'phone': '617-555-0112'},
        {'city': 'Atlanta',       'state': 'Georgia',       'zip': '30301', 'address': '1300 Peachtree St',   'full_name': 'Atlanta Auto Mall',     'phone': '404-555-0113'},
        {'city': 'Dallas',        'state': 'Texas',         'zip': '75201', 'address': '1400 Commerce St',    'full_name': 'Dallas Motor World',    'phone': '214-555-0114'},
        {'city': 'Portland',      'state': 'Oregon',        'zip': '97201', 'address': '1500 Burnside Ave',   'full_name': 'Portland Car Hub',      'phone': '503-555-0115'},
    ]

    created_dealers = []
    for d in dealers_data:
        dealer = Dealer.objects.create(**d)
        created_dealers.append(dealer)

    # Seed reviews (referencing dealers by index)
    reviews_data = [
        (0,  'Alice',   'Great service! Very friendly and helpful staff.',          True,  '2023-06-15', 'Toyota',       'Camry',    2023),
        (0,  'Bob',     'Average experience, nothing special.',                     False, '2023-04-20', 'Honda',        'Civic',    2022),
        (1,  'Carol',   'Fantastic services and amazing deals! Highly recommend!',  True,  '2023-08-10', 'Ford',         'Mustang',  2023),
        (2,  'Dave',    'Poor customer service, very disappointed.',                False, '2023-07-05', 'BMW',          '3 Series', 2022),
        (3,  'Eve',     'Excellent experience buying my new truck!',                True,  '2023-09-01', 'Chevrolet',    'Silverado',2023),
        (4,  'Frank',   'Neutral experience overall, nothing to complain about.',   False, '2023-05-18', 'Mercedes-Benz','C-Class',  2023),
        (5,  'Grace',   'Best dealership in California, highly recommend!',         True,  '2023-10-12', 'Toyota',       'RAV4',     2023),
        (6,  'Hank',    'Really happy with my purchase in New York!',               True,  '2023-11-20', 'Ford',         'F-150',    2023),
        (10, 'Iris',    'Great staff in Topeka! They went above and beyond.',       True,  '2023-12-01', 'Honda',        'CR-V',     2023),
        (10, 'Jack',    'Good selection of vehicles and fair pricing.',             True,  '2023-11-05', 'Chevrolet',    'Equinox',  2022),
    ]

    for idx, reviewer, text, purchase, date, make, model, year in reviews_data:
        Review.objects.create(
            dealer=created_dealers[idx],
            name=reviewer,
            review=text,
            purchase=purchase,
            purchase_date=date,
            car_make=make,
            car_model=model,
            car_year=year,
        )

    print(f"Seeded {len(created_dealers)} dealers and {len(reviews_data)} reviews.")
