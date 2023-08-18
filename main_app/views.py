from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Field, Dino
# from .forms import
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


@login_required
def fields_index(request):
    fields = Field.objects.filter(user=request.user)
    return render(request, 'fields/index.html', {'fields': fields})


@login_required
def fields_detail(request, field_id):
    field = Field.objects.get(id=field_id)
    dinos = field.dinos.all().values_list('id')
    return render(request, 'fields/detail.html', {'field': field, 'dinos': dinos})

@login_required
def dinos_detail(request, dino_id):
    dino = Dino.objects.get(id=dino_id)
    return render(request, 'dinos/detail.html', {'dino': dino})

