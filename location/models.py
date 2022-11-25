from django.db import models
from django.utils.text import slugify


class Province(models.Model):
    name = models.CharField(max_length=50, verbose_name="استان")
    slug = models.SlugField(max_length=50, allow_unicode='True', verbose_name="اسلاگ")

    def get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while Province.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'استان'
        verbose_name_plural = 'استان ها'


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name="شهر")
    slug = models.SlugField(max_length=50, allow_unicode='True', unique=True, blank=True, verbose_name="اسلاگ")
    state = models.ForeignKey(Province, related_name='cities', on_delete=models.CASCADE, verbose_name="استان")

    def get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while City.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "شهر"
        verbose_name_plural = "شهر ها"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('advertisement-list', args=[self.name])


class District(models.Model):
    name = models.CharField(max_length=50, verbose_name="محله")
    slug = models.SlugField(max_length=50, allow_unicode='True', verbose_name="اسلاگ")
    city = models.ForeignKey(City, related_name='districts', on_delete=models.CASCADE, verbose_name="شهر")

    def get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while District.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        self.slug = self.get_unique_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "محله"
        verbose_name_plural = "محله ها"


class Location(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name="استان")
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="شهر")
    district = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True, verbose_name="محله")

    def __str__(self):
        return f"{self.city} < {self.province}"

    class Meta:
        verbose_name = "موقعیت"
        verbose_name_plural = "موقعیت ها"
