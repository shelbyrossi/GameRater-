from django.db import models


class Rating(models.Model):
    
    game_id = models.ForeignKey("Game", on_delete=models.CASCADE)
    rating = models.CharField(max_length=30)
    player_id = models.ForeignKey("Player", on_delete=models.CASCADE)