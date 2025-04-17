from django.contrib import admin
from .models import Game

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('id', 'player_white', 'player_black', 'is_active', 'created_at')
    list_filter = ('is_active', 'created_at')
