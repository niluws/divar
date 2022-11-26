from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Advertisement
from django.utils.text import slugify


@receiver(pre_save, sender=Advertisement)
def create_post(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_unique_slug(instance)


def create_unique_slug(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title, allow_unicode=True)
    qs = Advertisement.objects.filter(slug=slug)
    if qs.exists():
        new_slug = f'{slug}-{qs.first().id}'
        return create_unique_slug(instance, new_slug)
    return slug
