from django.contrib import admin

from .models import Games, Player, Shoes, Photo

class PlayerAdmin(admin.ModelAdmin):
  readonly_fields = ('id',)

admin.site.register(Player, PlayerAdmin)
admin.site.register(Games)
admin.site.register(Shoes)
admin.site.register(Photo)
