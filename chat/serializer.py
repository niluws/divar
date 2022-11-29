from .models import Room, Message
from rest_framework import serializers


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['message_sender_id', 'message_receiver_id', 'message', 'date']


class RoomSerializer(serializers.ModelSerializer):
    message_set = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ["pk", 'advertisement', "date", 'message_set']
