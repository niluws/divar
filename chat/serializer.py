from .models import Room, Message
from rest_framework import serializers
from core.serializer import UserSerializer


class MessageSerializer(serializers.ModelSerializer):
    message_sender = UserSerializer(read_only=True)
    message_receiver = UserSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ['room', 'message_sender', 'message_receiver', 'message', 'date']


class RoomSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ["pk", 'advertisement', "date", 'messages']
