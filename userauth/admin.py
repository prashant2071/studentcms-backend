from django.contrib import admin
from userauth.models import User

# admin ko model ho vanera inform gareko
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "email","is_superuser","is_active"]
    
    
    # yo rakhiyoo vane listed field name matri change garna dinxa
    # fields=["course_name","instructor_name"]
    
    #we can use exclude only course_name if course name is in list
    # exclude = ["course_name"]

# course ma courseadmin register gareko
admin.site.register(User, UserAdmin)