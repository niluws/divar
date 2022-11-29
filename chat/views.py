from rest_framework.viewsets import ModelViewSet
from .serializer import RoomSerializer, MessageSerializer
from .models import Room, Message


class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get_serializer_context(self):
        return {'request': self.request}


class ChatViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_serializer_context(self):
        return {'request': self.request}
