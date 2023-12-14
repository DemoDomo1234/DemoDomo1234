from django.apps import AppConfig


class VideoConfig(AppConfig):
    name = 'video'

    def ready(self):
        import video.signals