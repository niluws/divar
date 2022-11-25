from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator
from location.models import Location
from category.models import Category

# To get user from settings
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
    slug = models.SlugField(null=False, verbose_name="اسلاگ", blank=True)

    def get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Advertisement.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} > {self.location.city.name}"

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
