import datetime
from random import shuffle
from django.db.models import F
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Field, Dino
from .forms import DinoForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

DINO_URLS = {
    ('Blue', 'https://i.imgur.com/dikM05s.gif'), 
    ('Pink', 'https://i.imgur.com/CamDYFr.gif'), 
    ('Grey', 'https://i.imgur.com/0bin3rQ.gif'), 
    ('Dark Blue', 'https://i.imgur.com/AS84RMX.gif'), 
    ('Light Grey', 'https://i.imgur.com/Uh8Bg49.gif'), 
    ('Red', 'https://i.imgur.com/c5XOuHP.gif'), 
    ('Orange', 'https://i.imgur.com/s5H4eOr.gif'), 
    ('Green', 'https://i.imgur.com/lTOcnhK.gif'), 
    ('Yellow', 'https://i.imgur.com/Ptsxyuv.gif'), 
    ('Dark Green', 'https://i.imgur.com/QRnJ2Fu.gif')
}

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
    dino_form = DinoForm()
    remaining_tiles = int(25 - len(field.dino_set.all()))
    current_date = datetime.datetime.now()

    # Calculates total focus time for a field
    total_secs = 0
    for dino in field.dino_set.all():
        mins, secs = map(int, dino.duration.split(":"))
        total_secs += mins * 60 + secs
    focus_time = f'{total_secs // 60}'

    return render(request, 'fields/detail.html', {'field': field, 'dino_form': dino_form, 'remaining_tiles': range(remaining_tiles), 'current_date': current_date, 'focus_time': focus_time})


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
def add_dino(request, field_id):
    form = DinoForm(request.POST)
    if form.is_valid():
        new_dino = form.save(commit=False)
        new_dino.field_id = field_id
        for colour, url in DINO_URLS:
            if colour == new_dino.colour:
                new_dino.url = url

        new_dino.save()
    return redirect('fields_detail', field_id=field_id)


@login_required
def dinos_detail(request, dino_id):
    dino = Dino.objects.get(id=dino_id)
    return render(request, 'dinos/detail.html', {
        'dino': dino,
    })


class DinoUpdate(LoginRequiredMixin, UpdateView):
    model = Dino
    fields = ['name']

class DinoDelete(LoginRequiredMixin, DeleteView):
    model = Dino

    def get_success_url(self):
        field = self.object.field
        return reverse_lazy('fields_detail', kwargs={'field_id': field.id})


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
