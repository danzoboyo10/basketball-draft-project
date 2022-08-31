from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from main_app.forms import GamesForm
from .models import Player, Shoes, Photo
from main_app.forms import GamesForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'bball-proj'


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def players_index(request):
  players = Player.objects.filter(user=request.user)
  return render(request, 'players/index.html', { 'players': players })

@login_required
def players_detail(request, player_id):
  player = Player.objects.get(id=player_id)
  shoes_player_doesnt_have = Shoes.objects.exclude(id__in = player.shoes.all().values_list('id'))
  games_form = GamesForm()
  return render(request, 'players/detail.html',{
    'player': player, 'games_form': games_form,
    'shoes': shoes_player_doesnt_have
    })


@login_required
def add_game(request, player_id):
  form = GamesForm(request.POST)
  if form.is_valid():
    new_game = form.save(commit=False)
    new_game.player_id = player_id
    new_game.save()
  return redirect('detail', player_id=player_id)


@login_required
def assoc_shoe(request, player_id, shoe_id):
  Player.objects.get(id=player_id).shoes.add(shoe_id)
  return redirect('detail', player_id=player_id)

@login_required
def assoc_shoe_delete(request, player_id, shoe_id):
  Player.objects.get(id=player_id).shoes.remove(shoe_id)
  return redirect('detail', player_id=player_id)

@login_required
def add_photo(request, player_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
      s3 = boto3.client('s3')
      key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
      try:
        s3.upload_fileobj(photo_file, BUCKET, key)
        url = f"{S3_BASE_URL}{BUCKET}/{key}"
        photo = Photo(url=url, player_id=player_id)
        photo.save()
        print(photo)
      except:
        print('An error occured uploading file to s3')
    return redirect('detail', player_id=player_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
  else:
    error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class PlayerCreate(LoginRequiredMixin, CreateView):
  model = Player
  fields = ['name', 'age', 'college', 'ppg']
  success_url = '/players/'

  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)



class PlayerUpdate(LoginRequiredMixin, UpdateView):
  model = Player
  fields = ['name', 'age', 'college', 'ppg']
  success_url = '/players/'
  

class PlayerDelete(LoginRequiredMixin, DeleteView):
  model = Player
  fields = '__all__'
  success_url = '/players/'

class ShoeList(LoginRequiredMixin, ListView):
  model = Shoes
  template_name = 'shoes/index.html'


class ShoeDetail(LoginRequiredMixin, DetailView):
  model = Shoes
  template_name = 'shoes/detail.html'


class ShoeCreate(LoginRequiredMixin, CreateView):
    model = Shoes
    fields = ['name', 'size']
    success_url = '/shoes/'

    def form_valid(self, form):
      form.instance.user = self.request.user  
      return super().form_valid(form)


class ShoeUpdate(LoginRequiredMixin, UpdateView):
  model = Shoes
  fields = ['name', 'size']
  success_url = '/shoes/'

class ShoeDelete(LoginRequiredMixin, DeleteView):
  model = Shoes
  fields = '__all__'
  success_url = '/shoes/'

  

