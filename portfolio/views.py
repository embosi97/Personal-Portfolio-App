from django.shortcuts import render
import requests
from .models import Project


# Create your views here.
def HomePage(request):
    #grabs all the projects objects from the DB
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'projects': projects})
