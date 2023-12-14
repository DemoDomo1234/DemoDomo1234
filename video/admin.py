from django.contrib import admin
from .models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "author",)
    list_filter = ("date", "author", "title",)
    search_fields = ("title", "author", "body",)

admin.site.register(Video, VideoAdmin)
