from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from golf_website.forms import GolfUserCreationForm, GolfUserChangeForm
from golf_website.models import GolfUser


class GolfUserAdmin(UserAdmin):
    add_form = GolfUserCreationForm
    form = GolfUserChangeForm
    model = GolfUser
    list_display = ["email", "username"]


admin.site.register(GolfUser, GolfUserAdmin)

