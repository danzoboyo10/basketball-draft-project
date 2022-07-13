from django.shortcuts import redirect, render
from main_app.forms import GamesForm
from .models import Player, Shoes, Photo
from main_app.forms import GamesForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'bball-proj'




def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def players_index(request):
  players = Player.objects.all()
  return render(request, 'players/index.html', { 'players': players })

def players_detail(request, player_id):
  player = Player.objects.get(id=player_id)
  games_form = GamesForm()
  return render(request, 'players/detail.html',{
    'player': player, 'games_form': games_form,
    })

def add_game(request, player_id):
  form = GamesForm(request.POST)
  if form.is_valid():
    new_game = form.save(commit=False)
    new_game.player_id = player_id
    new_game.save()
  return redirect('detail', player_id=player_id)



def assoc_shoe(request, player_id, shoe_id):
  Player.objects.get(id=player_id).shoes.add(shoe_id)
  return redirect('detail', player_id=player_id)

def assoc_shoe_delete(request, player_id, shoe_id):
  Player.objects.get(id=player_id).shoes.remove(shoe_id)
  return redirect('detail', player_id=player_id)

def add_photo(request, player_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, player_id=player_id)
      photo.save()
    except:
      print('An error occured uploading file to s3')
  return redirect('detail', player_id=player_id)



class PlayerCreate(CreateView):
  model = Player
  fields = '__all__'
  success_url = '/players/'

class PlayerUpdate(UpdateView):
  model = Player
  fields = '__all__'
  success_url = '/players/'

class PlayerDelete(DeleteView):
  model = Player
  fields = '__all__'
  success_url = '/players/'

class ShoeList(ListView):
  model = Shoes
  template_name = 'shoes/index.html'


class ShoeDetail(DetailView):
  model = Shoes
  template_name = 'shoes/detail.html'

class ShoeCreate (CreateView):
  model = Shoes
  fields = '__all__'
  template_name = 'shoes/index.html'


class ShoeUpdate(UpdateView):
  model = Shoes
  fields = ['name', 'size']

class ShoeDelete(DeleteView):
  model = Shoes
  success_url = '/shoes/'



  

