from django.contrib import admin
from .models import CarMake, CarModel, Dealer, Review


class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1


@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ['name', 'country_of_origin', 'description']
    search_fields = ['name']
    inlines = [CarModelInline]


@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'car_make', 'car_type', 'year', 'dealer_id']
    list_filter  = ['car_type', 'car_make', 'year']
    search_fields = ['name', 'car_make__name']


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0
    readonly_fields = ['name', 'review', 'purchase', 'car_make', 'car_model', 'car_year']


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display  = ['full_name', 'city', 'state', 'zip', 'phone']
    list_filter   = ['state']
    search_fields = ['full_name', 'city', 'state']
    inlines       = [ReviewInline]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display  = ['name', 'dealer', 'car_make', 'car_model', 'car_year', 'purchase']
    list_filter   = ['purchase', 'car_make']
    search_fields = ['name', 'review', 'dealer__full_name']
