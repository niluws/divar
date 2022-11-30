from django.db import models
from django.conf import settings
import uuid
from datetime import datetime
from advertisement.models import Advertisement



class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField(default=datetime.now)
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"Room({self.id})"


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    message_sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='%(class)s_sender')
    message_receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='%(class)s_receiver')
    message = models.TextField()
    date = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"Message({self.message} ( from {self.message_sender} to {self.message_receiver}))"
