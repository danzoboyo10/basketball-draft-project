from django.shortcuts import redirect, render
from main_app.forms import GamesForm
from .models import Player, Shoes
from main_app.forms import GamesForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView






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



  

