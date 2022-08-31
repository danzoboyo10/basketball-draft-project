from django.contrib import admin

from .models import Games, Player, Shoes, Photo

admin.site.register(Player)
admin.site.register(Games)
admin.site.register(Shoes)
admin.site.register(Photo)
