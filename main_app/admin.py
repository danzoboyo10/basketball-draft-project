from django.contrib import admin

from .models import Games, Player

admin.site.register(Player)

admin.site.register(Games)