from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from location.models import City,District,Province
from category.models import Category

User = get_user_model()


class Advertisement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    title = models.CharField(max_length=50, verbose_name='موضوع')
    description = models.TextField(blank=True, verbose_name="توضیحات")
    price = models.PositiveIntegerField(default=0, verbose_name="قیمت")
    province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name="استان")
    city = models.ForeignKey(City, on_delete=models.CASCADE,verbose_name="شهر")
    district = models.ForeignKey(District, on_delete=models.CASCADE, verbose_name="محله")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,verbose_name='دسته')
    is_active_chat = models.BooleanField(verbose_name="چت دیوار فعال شود", default=True)
    is_show_phone = models.BooleanField(verbose_name="شماره تلفن در آگهی نمایش داده نشود", default=False)
    slug = models.SlugField(verbose_name="اسلاگ", allow_unicode=True, editable=False)

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
