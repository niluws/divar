from django.apps import AppConfig


class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'advertisement'
    verbose_name = 'آگهی ها'

    def ready(self):
        import advertisement.signals

