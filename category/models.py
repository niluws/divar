from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="دسته")
    slug = models.SlugField(max_length=200, null=True, blank=True, allow_unicode=True, verbose_name="اسلاگ")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'دسته'
        verbose_name_plural = "دسته ها"
