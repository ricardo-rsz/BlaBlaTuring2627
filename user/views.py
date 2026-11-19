from django.shortcuts import render

# Create your views here.

from .models import User

from django.views.generic.list import ListView

from django.views.generic.detail import DetailView

def index(request):
    pass

class UserListView(ListView):
    model = User

class UserDetailView(DetailView):
    model = User