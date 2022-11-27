from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('messages', views.MessageViewSet)

urlpatterns = router.urls
