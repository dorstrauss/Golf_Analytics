from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from golf_website.models import GolfUser


class GolfUserCreationForm(UserCreationForm):

    class Meta:
        model = GolfUser
        fields = ("username", "email")


class GolfUserChangeForm(UserChangeForm):

    class Meta:
        model = GolfUser
        fields = ("username", "email")
