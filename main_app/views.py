from django.shortcuts import redirect, render, redirect
from main_app.forms import GamesForm
from .models import Player
from main_app.forms import GamesForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView




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
  
def add_game(request, player_id):
  form = GamesForm(request.POST)
  if form.is_valid():
    new_game = form.save(commit=False)
    new_game.player_id = player_id
    new_game.save()
  return redirect('detail', player_id=player_id)

