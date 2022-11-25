from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('advertisement.urls')),
    path('location/', include('location.urls')),
    path('category/', include('category.urls')),
]
