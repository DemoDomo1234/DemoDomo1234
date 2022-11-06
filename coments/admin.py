from django.contrib import admin
from .models import Coments

class ComentsAdmin(admin.ModelAdmin):
    list_display = ("date", "author",)
    list_filter = ("date", "author", "body",)
    search_fields = ("date", "author", "body",)

admin.site.register(Coments, ComentsAdmin)