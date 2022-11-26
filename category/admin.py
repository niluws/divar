from django.contrib import admin
from .models import Category


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    fields = ('category', 'parent')
    readonly_fields = ['slug']
    list_display = ('category', 'parent', 'slug')
