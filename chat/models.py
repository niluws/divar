from django.db import models
from django.conf import settings
import uuid
from datetime import datetime
from advertisement.models import Advertisement


class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField(default=datetime.now, verbose_name='تاریخ')
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, verbose_name="آگهی")

    class Meta:
        verbose_name = 'اتاق'
        verbose_name_plural = "اتاق ها"
        ordering = ['-date']

    def __str__(self):
        return f"Room({self.id})"


class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='اتاق', related_name='messages')
    message_sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                       verbose_name='ارسال کننده',related_name='message_sender')
    message_receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                         verbose_name='دریافت کننده',related_name='message_receiver')
    message = models.TextField(verbose_name='پیام')
    date = models.DateTimeField(default=datetime.now, verbose_name='تاریخ')

    class Meta:
        verbose_name = 'پیام'
        verbose_name_plural = "پیام ها"
        ordering = ['date']

    def __str__(self):
        return f"Message({self.message} ( from {self.message_sender} to {self.message_receiver}))"
