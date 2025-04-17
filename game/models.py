from django.db import models
from django.contrib.auth.models import User

class Game(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    player_white = models.ForeignKey(User, related_name='white_games', on_delete=models.CASCADE)
    player_black = models.ForeignKey(User, related_name='black_games', on_delete=models.CASCADE, null=True, blank=True)
    fen = models.CharField(max_length=100, default="startpos")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}: {self.player_white} vs {self.player_black or 'Waiting...'}"

    def get_player_color(self, user):
        if user == self.player_white:
            return "white"
        elif user == self.player_black:
            return "black"
        return "spectator"