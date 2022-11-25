from django.contrib import admin
from .models import Category


@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    fields = ('name', 'parent')
    readonly_fields = ['slug']
    list_display = ('name', 'parent', 'slug')
