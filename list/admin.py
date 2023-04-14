from django.contrib import admin
from .models import List, PlayList


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
