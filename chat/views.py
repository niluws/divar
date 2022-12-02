from rest_framework.viewsets import ModelViewSet
from .serializer import RoomSerializer, MessageSerializer
from .models import Room, Message
from rest_framework import permissions


class RoomViewSet(ModelViewSet):
    serializer_class = RoomSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = Room.objects.filter(advertisement__user_id=user)
        return queryset


class ChatViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    def get_serializer_context(self):
        return {'request': self.request}

