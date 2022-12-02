from django.contrib import admin
from .models import Advertisement, AdvertisementImage


class AdvertisementImageInline(admin.TabularInline):
    model = AdvertisementImage


@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title', 'category','slug')
    inlines = [
        AdvertisementImageInline
    ]

