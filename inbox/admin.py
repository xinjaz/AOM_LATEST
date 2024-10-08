from django.contrib import admin
from django.contrib.auth.models import User


# Define a custom UserAdmin class to display users
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'is_superuser')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('is_active', 'is_superuser')


# Unregister the default User admin
admin.site.unregister(User)

# Register the User model with the custom UserAdmin
admin.site.register(User, UserAdmin)
