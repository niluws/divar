from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Advertisement
from django.utils.text import slugify


@receiver(pre_save, sender=Advertisement)
def create_post(sender, instance, *args, **kwargs):
    if not instance.advslug:
        instance.advslug = create_unique_slug(instance)


def create_unique_slug(instance, new_advslug=None):
    if new_advslug is not None:
        advslug = new_advslug
        print(advslug)
    else:
        advslug = slugify(instance.title, allow_unicode=True)
        print(advslug)
    qs = Advertisement.objects.filter(advslug=advslug)
    print(qs)
    if qs.exists():
        print(qs.last())
        new_advslug = f'{advslug}-{qs.first().id}'
        return create_unique_slug(instance, new_advslug)
    return advslug



