from django.db import models


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, default='')
    country_of_origin = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Car Make"
        verbose_name_plural = "Car Makes"


class CarModel(models.Model):
    CAR_TYPES = [
        ('SEDAN', 'Sedan'), ('SUV', 'SUV'), ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'), ('CONVERTIBLE', 'Convertible'),
        ('TRUCK', 'Truck'), ('VAN', 'Van'), ('HATCHBACK', 'Hatchback'),
    ]
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='car_models')
    name = models.CharField(max_length=100)
    car_type = models.CharField(max_length=20, choices=CAR_TYPES, default='SEDAN')
    year = models.IntegerField(default=2023)
    dealer_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.car_make.name} {self.name} ({self.year})"

    class Meta:
        verbose_name = "Car Model"
        verbose_name_plural = "Car Models"


class Dealer(models.Model):
    """Stores dealer info locally in SQLite (no Node/Mongo needed)."""
    city      = models.CharField(max_length=100)
    state     = models.CharField(max_length=100)
    zip       = models.CharField(max_length=20, blank=True, default='')
    address   = models.CharField(max_length=200, blank=True, default='')
    full_name = models.CharField(max_length=200)
    phone     = models.CharField(max_length=50, blank=True, default='')

    def __str__(self):
        return f"{self.full_name} ({self.city}, {self.state})"

    def to_dict(self):
        return {
            'id':        self.pk,
            'city':      self.city,
            'state':     self.state,
            'zip':       self.zip,
            'address':   self.address,
            'full_name': self.full_name,
            'phone':     self.phone,
        }

    class Meta:
        verbose_name = "Dealer"
        verbose_name_plural = "Dealers"


class Review(models.Model):
    """Stores reviews locally in SQLite."""
    dealer        = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='reviews')
    name          = models.CharField(max_length=100)
    review        = models.TextField()
    purchase      = models.BooleanField(default=False)
    purchase_date = models.CharField(max_length=50, blank=True, default='')
    car_make      = models.CharField(max_length=100, blank=True, default='')
    car_model     = models.CharField(max_length=100, blank=True, default='')
    car_year      = models.IntegerField(default=2023)

    def __str__(self):
        return f"Review by {self.name} for {self.dealer.full_name}"

    def to_dict(self):
        return {
            'id':            self.pk,
            'name':          self.name,
            'dealership':    self.dealer_id,
            'review':        self.review,
            'purchase':      self.purchase,
            'purchase_date': self.purchase_date,
            'car_make':      self.car_make,
            'car_model':     self.car_model,
            'car_year':      self.car_year,
        }

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
