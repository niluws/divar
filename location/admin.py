from django.contrib import admin
from .models import Location, Province, City, District


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    # fields = ['name']
    # readonly_fields = ['slug']
    # list_editable = 'name'
    list_display = ('province', 'slug')
    prepopulated_fields = {
        'slug': ['province']
    }


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    fields = ['city', 'province']
    readonly_fields = ['slug']
    list_display = ('city', 'slug', 'province')



@admin.register(District)
class DistinctAdmin(admin.ModelAdmin):
    fields = ['district', 'city']
    readonly_fields = ['slug']
    list_display = ('district', 'slug', 'city')
