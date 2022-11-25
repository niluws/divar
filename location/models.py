from django.db import models


class Province(models.Model):
    name = models.CharField(max_length=50, verbose_name="اسم",unique=True)
    slug = models.SlugField(verbose_name="اسلاگ", allow_unicode=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'استان'
        verbose_name_plural = 'استان ها'


class City(models.Model):
    name = models.CharField(max_length=50, verbose_name="اسم")
    slug = models.SlugField(verbose_name="اسلاگ", allow_unicode=True)
    state = models.ForeignKey(Province, related_name='cities', on_delete=models.CASCADE, verbose_name="استان")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "شهر"
        verbose_name_plural = "شهر ها"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('advertisement-list', args=[self.name])


class District(models.Model):
    name = models.CharField(max_length=50, verbose_name="اسم")
    slug = models.SlugField(verbose_name="اسلاگ", allow_unicode=True)
    city = models.ForeignKey(City, related_name='districts', on_delete=models.CASCADE, verbose_name="شهر")

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
