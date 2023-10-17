from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from golf_website.models import GolfUser


class GolfUserCreationForm(UserCreationForm):

    class Meta:
        model = GolfUser
        fields = ('first_name', 'last_name', 'email', 'sensor_id')



class GolfUserChangeForm(UserChangeForm):

    class Meta:
        model = GolfUser
        fields = ("username", "email")
