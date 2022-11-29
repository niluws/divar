from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('rooms', views.RoomViewSet)
router.register('messages', views.ChatViewSet)
urlpatterns = router.urls
