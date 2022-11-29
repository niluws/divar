from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('rooms', views.RoomViewSet)
router.register('rooms', views.ChatViewSet)
urlpatterns = router.urls
