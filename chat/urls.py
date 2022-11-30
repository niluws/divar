from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from . import views
from advertisement.views import AdvertisementViewSet

router = DefaultRouter()
router.register('rooms', views.RoomViewSet,basename='rooms')
router.register('messages', views.ChatViewSet)

# chat_router = routers.NestedDefaultRouter(router, 'rooms', lookup='rooms')
# chat_router.register('messages', views.ChatViewSet, basename='messages')
urlpatterns = router.urls
