from distutils.command.upload import upload
from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

OPTIONS = (
    ('A', 'Away'),
    ('H', 'Home'),
    ('P', 'Playoffs')
)

# Create your models here.

class Shoes(models.Model):
  name = models.CharField(max_length=50)
  size = models.FloatField(null = True)
 
  def __str__(self):
    return f'{self.name} {self.size}'

  def get_absolute_url(self):
    return reverse('shoes_detail', kwargs={'shoe_id': self.id})

class Player(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    height = models.CharField(max_length= 50, null=True)
    weight = models.CharField(max_length=50, null=True)
    college = models.CharField(max_length=50, null=True)
    ppg = models.FloatField(null= True)
    apg = models.FloatField(null= True)
    rpg = models.FloatField(null= True) 
    spg = models.FloatField(null= True)
    per = models.FloatField(null = True)
    shoes = models.ManyToManyField(Shoes)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    
    def no_more_games_today(self):
      return self.games_set.filter(date=date.today()).count() >= len(OPTIONS)

    def __str__(self):
      return self.name

    def get_absolute_url(self):
      return reverse('detail', kwargs={'player_id': self.id})

class Games(models.Model):
  date = models.DateField()
  game = models.CharField(
      max_length=1,
      choices=OPTIONS,
      default=OPTIONS[0][0]
  )

  player = models.ForeignKey(Player, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_game_display()} on {self.date}"

  
  class Meta:
    ordering = ['-date']

class Photo(models.Model):
  url = models.CharField(max_length=200)
  player = models.ForeignKey(Player, on_delete=models.CASCADE)


  def __str__(self):
    return f"Photo for player_id: {self.player_id} @{self.url}"



