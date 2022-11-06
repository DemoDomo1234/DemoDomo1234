from django.apps import AppConfig


class ComentsConfig(AppConfig):
    name = 'coments'

    def ready(self):
        import coments.signals