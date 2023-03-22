from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUp

# Create your views here.h
def home(request):
    return render(request, "index.html")

def welcome(request):
    return render(request, "welcome.html")

@login_required
def profile(request):
    return render(request, "profile.html")

class SignUpView(CreateView):
    form_class = SignUp
    success_url = reverse_lazy("login")
    template_name = "signup.html"