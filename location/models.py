from django.db import models


class Province(models.Model):
    province = models.CharField(max_length=50, verbose_name="اسم",unique=True)
    slug = models.SlugField(verbose_name="اسلاگ", allow_unicode=True)

    def __str__(self):
        return f"{self.province}"

    class Meta:
        verbose_name = 'استان'
        verbose_name_plural = 'استان ها'


class City(models.Model):
    city = models.CharField(max_length=50, verbose_name="اسم")
    slug = models.SlugField(verbose_name="اسلاگ", allow_unicode=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name="استان",related_name="cities")

    def __str__(self):
        return f"{self.city}"

    class Meta:
        verbose_name = "شهر"
        verbose_name_plural = "شهر ها"



class District(models.Model):
    district = models.CharField(max_length=50, verbose_name="اسم")
    slug = models.SlugField(verbose_name="اسلاگ", allow_unicode=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="شهر")

    def __str__(self):
        return f"{self.district}"

    class Meta:
        verbose_name = "محله"
        verbose_name_plural = "محله ها"


class Location(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name="استان")
    city = models.ForeignKey(City, on_delete=models.CASCADE, verbose_name="شهر")
    district = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True, verbose_name="محله")

    def __str__(self):
        return f"{self.city} < {self.province}"

    class Meta:
        verbose_name = "موقعیت"
        verbose_name_plural = "موقعیت ها"

