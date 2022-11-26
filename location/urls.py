from django.urls import path
from . import views

urlpatterns = [
    path('provinces/', views.ProvinceView.as_view()),
    path('cities/', views.CityView.as_view()),
    path('district/', views.DistrictView.as_view()),
]

