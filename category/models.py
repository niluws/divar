from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=50, verbose_name="دسته")
    slug = models.SlugField(verbose_name="اسلاگ", allow_unicode=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategory')

    def __str__(self):
        return f"{self.category}"

    class Meta:
        verbose_name = 'دسته'
        verbose_name_plural = "دسته ها"

