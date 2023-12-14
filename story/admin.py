from django.contrib import admin
from .models import Story



class StoryAdmin(admin.ModelAdmin):
    list_display = ("user",)
    list_filter = ("created", "user",)
    search_fields = ("title", "user", "body",)

admin.site.register(Story, StoryAdmin)
