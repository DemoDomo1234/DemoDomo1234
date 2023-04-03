from django.contrib import admin
from .models import Blog


class BlogAdmin(admin.ModelAdmin):
    list_display = ("titel", "author",)
    list_filter = ("date", "author", "titel",)
    search_fields = ("titel", "author", "body",)

admin.site.register(Blog, BlogAdmin)
