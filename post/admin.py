from django.contrib import admin
from .models import Post, Image


class PostAdmin(admin.ModelAdmin):
    list_display = ("user",)
    list_filter = ("time", "user",)
    search_fields = ("titel", "user", "body",)

admin.site.register(Post, PostAdmin)


class ImageAdmin(admin.ModelAdmin):
    list_display = ("time",)
    list_filter = ("time",)
    search_fields = ("time",)

admin.site.register(Image, ImageAdmin)