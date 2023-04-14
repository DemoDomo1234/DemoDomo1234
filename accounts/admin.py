from django.contrib import admin
from .models import User, Following, OTPCode

class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "name",)
    list_filter = ("email", "name",)
    search_fields = ("email", "name", "body",)

admin.site.register(User, UserAdmin)
admin.site.register(OTPCode)