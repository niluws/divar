from .models import Room, Message
from rest_framework import serializers
from core.models import User


class MessageSerializer(serializers.ModelSerializer):
    message_sender = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
    )
    message_receiver = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
    )

    class Meta:
        model = Message
        fields = ['room', 'message_sender', 'message_receiver', 'message', 'date']


class RoomSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ["pk", 'advertisement', "date", 'messages']
