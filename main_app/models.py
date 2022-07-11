from django.db import models

# Create your models here.
class Player:
  def __init__(self, name, age, college, ppg):
    self.name = name
    self.age = age
    self.college = college
    self.ppg = ppg

players = [
  Player('Tim', '23', 'ohio state', '30.9'),
  Player('Jim', '24', 'ball state', '20.9'),
  Player('Larry', '26', 'missouri state', '22.0'),
  Player('Gary', '29', 'oklahoma state', '24'),
]