import datetime
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Field, Dino, Animation
from .forms import DinoForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# URLs and image URLs for different colored dinos
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

# Home page view
def home(request):
    return render(request, 'home.html')

# About page view
def about(request):
    return render(request, 'about.html')

# List of fields view (requires login)
@login_required
def fields_index(request):
    fields = Field.objects.filter(user=request.user).order_by('-date')

    # Calculates total focus time for a field
    focus_times = []
    for field in fields:
        total_secs = 0
        for dino in field.dino_set.all():
            mins, secs = map(int, dino.duration.split(":"))
            total_secs += mins * 60 + secs
        field.duration = f'{total_secs // 60}'
        field.save()

        # Save date and focus time to array for graph display
        focus_times.append([field.date.strftime('%m/%d'), field.duration])

    current_date = datetime.datetime.now()
    return render(request, 'fields/index.html', {'fields': fields, 'current_date': current_date, 'focus_times': focus_times})

# Field detail view (requires login)
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

# Create a new field view (requires login)
class FieldCreate(LoginRequiredMixin, CreateView):
    model = Field
    fields = ['date']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# Delete field (requires login)
class FieldDelete(LoginRequiredMixin, DeleteView):
    model = Field
    success_url = '/fields'

# Add a dino view (requires login)
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

# Dino detail view (requires login)
@login_required
def dinos_detail(request, dino_id):
    dino = Dino.objects.get(id=dino_id)
    field = dino.field

    # Finds all animations that haven't been added to the dino yet
    id_list = dino.animations.all().values_list('id')
    available_animations = Animation.objects.exclude(id__in=id_list)

    # Calculates focus time in minutes
    mins, secs = map(int, dino.duration.split(":"))
    focus_time = f'{(mins * 60 + secs) // 60}'

    return render(request, 'dinos/detail.html', {
        'dino': dino,
        'field': field,
        'focus_time': focus_time,
        'available_animations': available_animations
    })

# Update a dino name and colour (requires login)
class DinoUpdate(LoginRequiredMixin, UpdateView):
    model = Dino
    fields = ['name', 'colour']

    def form_valid(self, form):
        dino = form.save(commit=False)
        color = form.cleaned_data['colour']
        for c, url in DINO_URLS:
            if c == color:
                dino.url = url
                break
        dino.save()

        return redirect('dinos_detail', dino.id)

# Delete a dino 
class DinoDelete(LoginRequiredMixin, DeleteView):
    model = Dino

    def get_success_url(self):
        field = self.object.field
        return reverse_lazy('fields_detail', kwargs={'field_id': field.id})


# Associate an animation with a dino view
@login_required
def assoc_animation(request, dino_id):
    dino = Dino.objects.get(id=dino_id)
    animation_id = request.POST.get('animation_id')
    if animation_id:
        animation = Animation.objects.get(id=animation_id)
        dino.animations.add(animation)
    return redirect('dinos_detail', dino_id=dino_id)


# User signup view
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