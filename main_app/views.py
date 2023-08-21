import os
import uuid
import boto3
import datetime
import random
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Field, Dino
from django.http import JsonResponse
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
    current_date = datetime.datetime.now()
    return render(request, 'fields/index.html', {'fields': fields, 'current_date': current_date})


@login_required
def fields_detail(request, field_id):
    field = Field.objects.get(id=field_id)
    # dinos = Field.dinos.all().values_list('id')
    current_date = datetime.datetime.now().date()
    return render(request, 'fields/detail.html', {'field': field, 'current_date': current_date})


class FieldCreate(LoginRequiredMixin, CreateView):
    model = Field
    fields = ['date']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class FieldDelete(LoginRequiredMixin, DeleteView):
    model = Field
    success_url = '/fields'


@login_required
def dinos_detail(request, dino_id):
    dino = Dino.objects.get(id=dino_id)
    return render(request, 'dinos/detail.html', {'dino': dino})


def hatch_dino(request):
    response_data = {'success': False, 'message': 'An error occurred.'}
    specific_dino_url = "https://i.imgur.com/OLfpwzO.gif"  

    if request.method == 'POST':
        fields = Field.objects.filter(user=request.user, hatched_dino__isnull=True)

        if fields.exists():
            random_field = random.choice(fields)
            available_dinos = Dino.objects.filter(field__isnull=True, url=specific_dino_url)

            if available_dinos.exists():
                specific_dino = available_dinos.first()
                random_field.hatched_dino = specific_dino
                random_field.save()

                response_data = {'success': True, 'message': 'Dino hatched successfully.'}
            else:
                response_data['message'] = 'No available dinos to hatch.'
        else:
            response_data['message'] = 'No empty fields available.'
    else:
        response_data['message'] = 'Invalid request method.'

    return JsonResponse(response_data)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
