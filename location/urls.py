from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('cities', views.CityView)
router.register('provinces', views.ProvinceView)
urlpatterns = router.urls
