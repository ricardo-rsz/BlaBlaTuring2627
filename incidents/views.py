from django.shortcuts import render
from .models import Incident
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Create your views here.

def index(request):
    pass

class IncidentsListView(ListView):
    model = Incident

class IncidentsDetailView(DetailView):
    model = Incident
    #template_name = "Incidents/incident_detail.html"