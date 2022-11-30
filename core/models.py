from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    phone_regex = RegexValidator(regex='^09[0-3][0-9]-?[0-9]{3}-?[0-9]{4}',
                                 message="Phone number must be entered in the format: '0999 999 9999'. Up to 11 digits allowed.")
    username = models.CharField(verbose_name='نام کاربری', max_length=50, unique=True, null=True)
    phone_number = models.CharField(verbose_name='شماره تلفن', validators=[phone_regex], max_length=11, null=True,
                                    unique=True)
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
