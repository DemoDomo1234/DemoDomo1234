from django.apps import AppConfig


class ShortConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'short'

    def ready(self):
        import short.signals
