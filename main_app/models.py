from django.db import models
from django.urls import reverse
from datetime import date

GAMEOPTIONS = (
    ('A', 'Away'),
    ('H', 'Home'),
    ('P', 'Playoffs')
)

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    college = models.CharField(max_length=50)
    ppg = models.IntegerField()

    def no_more_games_today(self):
      return self.games_set.filter(date=date.today()).count() >= len(GAMEOPTIONS
    )

    def __str__(self):
      return self.name

    def get_absolute_url(self):
      return reverse('detail', kwargs={'player_id': self.id})

class Games(models.Model):
  date = models.DateField('Game date')
  game = models.CharField(
      max_length=1,
    choices=GAMEOPTIONS
  ,
    default=GAMEOPTIONS
  [0][0]
  )

  player = models.ForeignKey(Player, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_game_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']




