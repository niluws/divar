from django.urls import path
from .views import CityProvinceView

urlpatterns = [
    path('', CityProvinceView.as_view(), name='cities'),
]
