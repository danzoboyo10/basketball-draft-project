from django.contrib import admin

from .models import Games, Player, Shoes

admin.site.register(Player)

admin.site.register(Games)

admin.site.register(Shoes)