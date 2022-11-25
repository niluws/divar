from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import District, City
from django.utils.text import slugify


@receiver(pre_save, sender=District)
def create_post(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_unique_slug(instance)


def create_unique_slug(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.name, allow_unicode=True)
    qs = District.objects.filter(slug=slug)
    if qs.exists():
        new_slug = f'{slug}-{qs.first().id}'
        return create_unique_slug(instance, new_slug)
    return slug


@receiver(pre_save, sender=City)
def create_post(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_unique_slug_city(instance)


def create_unique_slug_city(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.name, allow_unicode=True)
    qs = City.objects.filter(slug=slug)
    if qs.exists():
        new_slug = f'{slug}-{qs.first().id}'
        return create_unique_slug(instance, new_slug)
    return slug
