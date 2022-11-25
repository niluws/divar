from django.contrib import admin
from .models import Location, Province, City, District


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    fields = ['name']
    readonly_fields = ['slug']
    list_display = ('name', 'slug')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    fields = ['name', 'state']
    readonly_fields = ['slug']
    list_display = ('name', 'slug', 'state')


@admin.register(District)
class DistinctAdmin(admin.ModelAdmin):
    fields = ['name', 'city']
    readonly_fields = ['slug']
    list_display = ('name', 'slug', 'city')
