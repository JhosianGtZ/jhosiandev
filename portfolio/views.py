from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Project


def index(request):
    projects = Project.objects.all()
    return render(request, "index.html", {'projects': projects})
