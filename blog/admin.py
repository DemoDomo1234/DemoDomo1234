from django.contrib import admin
from .models import (Blog, Story, Short, Post, List, PlayList, Image)

class BlogAdmin(admin.ModelAdmin):
    list_display = ("titel", "author",)
    list_filter = ("date", "author", "titel",)
    search_fields = ("titel", "author", "body",)

admin.site.register(Blog, BlogAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ("user",)
    list_filter = ("time", "user",)
    search_fields = ("titel", "user", "body",)

admin.site.register(Post, PostAdmin)

class StoryAdmin(admin.ModelAdmin):
    list_display = ("user",)
    list_filter = ("time", "user",)
    search_fields = ("titel", "user", "body",)

admin.site.register(Story, StoryAdmin)

class ShortAdmin(admin.ModelAdmin):
    list_display = ("user",)
    list_filter = ("time", "user",)
    search_fields = ("titel", "user", "body",)

admin.site.register(Short, ShortAdmin)

class ListAdmin(admin.ModelAdmin):
    list_display = ("user",)
    list_filter = ("time", "user",)
    search_fields = ("titel", "user", "body",)

admin.site.register(List, ListAdmin)

class PlayListAdmin(admin.ModelAdmin):
    list_display = ("user",)
    list_filter = ("time", "user",)
    search_fields = ("titel", "user", "body",)

admin.site.register(PlayList, PlayListAdmin)

class ImageAdmin(admin.ModelAdmin):
    list_display = ("time",)
    list_filter = ("time",)
    search_fields = ("time",)

admin.site.register(Image, ImageAdmin)