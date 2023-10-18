from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from golf_website.forms import GolfUserCreationForm


class SignUpView(CreateView):
    form_class = GolfUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'