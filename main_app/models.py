from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    college = models.CharField(max_length=50)
    ppg = models.IntegerField()

    def __str__(self):
      return self.name





# players = [
#   Player('Tim', '23', 'ohio state', '30.9'),
#   Player('Jim', '24', 'ball state', '20.9'),
#   Player('Larry', '26', 'missouri state', '22.0'),
#   Player('Gary', '29', 'oklahoma state', '24'),
# ]