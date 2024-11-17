from django.contrib import admin

from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["email", "first_name", "last_name", "address", "phone"]
    list_editable = ["phone"]
    search_fields = ["email", "first_name", "last_name", "address"]


admin.site.register(UserProfile, UserProfileAdmin)