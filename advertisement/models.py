from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from location.models import Location
from category.models import Category

User = get_user_model()


class Advertisement(models.Model):
    nationality_choices = (("ایرانی", "ایرانی"), ("اتباع خارجی", "اتباع خارجی"))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    title = models.CharField(max_length=50, verbose_name='موضوع')
    description = models.TextField(blank=True, verbose_name="توضیحات")
    price = models.PositiveIntegerField(default=0, verbose_name="قیمت")
    location = models.ForeignKey(Location, on_delete=models.CASCADE,
                                 verbose_name='موقعیت')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='دسته')
    melicode = models.CharField(max_length=10, verbose_name='کد ملی')
    nationality = models.CharField(max_length=13, choices=nationality_choices, default='ایرانی', verbose_name="ملیت")
    is_active_chat = models.BooleanField(verbose_name="چت دیوار فعال شود", default=True)
    is_show_phone = models.BooleanField(verbose_name="شماره تلفن در آگهی نمایش داده نشود", default=False)
    advslug = models.SlugField(verbose_name="اسلاگ", allow_unicode=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'آگهی'
        verbose_name_plural = "آگهی ها"


class AdvertisementImage(models.Model):
    advertisement = models.ForeignKey(
        Advertisement, on_delete=models.CASCADE, verbose_name="آگهی"
    )
    image_file = models.FileField(
        upload_to='images/advertisement/',
        validators=[FileExtensionValidator(allowed_extensions=('jpg', 'png', 'jpeg'))],
        verbose_name="عکس"
    )
