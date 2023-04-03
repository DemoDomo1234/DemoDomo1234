from django.contrib import admin
from .models import Story



class StoryAdmin(admin.ModelAdmin):
    list_display = ("user",)
    list_filter = ("time", "user",)
    search_fields = ("titel", "user", "body",)

admin.site.register(Story, StoryAdmin)
