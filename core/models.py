from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(verbose_name='نام کاربری', max_length=50, unique=True, null=True)
    phone_number = models.CharField(verbose_name='شماره تلفن', max_length=14, null=True, unique=True)
    Address = models.CharField(verbose_name='آدرس', max_length=100, null=True)
    Age = models.IntegerField(verbose_name='سن', default=0, null=True)
    mellicode = models.CharField(verbose_name='کدملی', max_length=10, null=True)
    email = models.EmailField(verbose_name='ایمیل', max_length=50, null=True, blank=True)
    is_admin = models.BooleanField(default=False, verbose_name='ادمین')

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربرها'

    def __str__(self):
        return self.username


class PhoneOtp(models.Model):
    phone_number = models.CharField(max_length=14, unique=True, default=None)
    otpcode = models.CharField(max_length=4, null=True, blank=True)
    token = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.phone_number
