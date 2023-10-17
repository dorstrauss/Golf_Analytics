from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from golf_website.forms import GolfUserCreationForm, GolfUserChangeForm
from golf_website.models import GolfUser


class GolfUserAdmin(UserAdmin):
    add_form = GolfUserCreationForm
    form = GolfUserChangeForm
    model = GolfUser
    list_display = ['username', 'email', 'sensor_id', 'height', 'handicap', 'player_image']

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Custom Fields',
            {
                'fields': ('sensor_id', 'player_image', 'height', 'handicap'),
            },
        ),
    )


admin.site.register(GolfUser, GolfUserAdmin)

