from django.contrib import admin
from accounts.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "first_name","last_name","email","password","phone"]


admin.site.register(Profile, ProfileAdmin)

# Register your models here.
