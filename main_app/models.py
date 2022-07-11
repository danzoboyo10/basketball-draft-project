from django.db import models
from django.urls import reverse

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    college = models.CharField(max_length=50)
    ppg = models.IntegerField()

    def __str__(self):
      return self.name

    def get_absolute_url(self):
      return reverse('detail', kwargs={'player_id': self.id})


