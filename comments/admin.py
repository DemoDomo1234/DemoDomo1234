from django.contrib import admin
from .models import Comments


class CommentsAdmin(admin.ModelAdmin):
    list_display = ("date", "author",)
    list_filter = ("date", "author", "body",)
    search_fields = ("date", "author", "body",)


admin.site.register(Comments, CommentsAdmin)