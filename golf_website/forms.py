from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from golf_website.models import GolfUser


class GolfUserCreationForm(UserCreationForm):

    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    height = forms.IntegerField(required=False)
    handicap = forms.IntegerField(required=False)
    player_image = forms.ImageField(required=False)

    class Meta:
        model = GolfUser
        fields = ('first_name', 'last_name', 'email', 'sensor_id', 'height', 'handicap', 'player_image')


class GolfUserChangeForm(UserChangeForm):

    sensor_id = forms.CharField()

    class Meta:
        model = GolfUser
        fields = ('first_name', 'last_name', 'email', 'sensor_id', 'height', 'handicap', 'player_image')
