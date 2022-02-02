from django.db import models


class Review(models.Model):
    
    game_id = models.ForeignKey("Game", on_delete=models.CASCADE)
    content = models.CharField(max_length=30)
    player_id = models.ForeignKey("Player", on_delete=models.CASCADE)