from django.db import models


class Photo(models.Model):
    
    photos_url = models.CharField(max_length=300)
    game_id = models.ForeignKey("Game", on_delete=models.CASCADE)
    player_id = models.ForeignKey("Player", on_delete=models.CASCADE)
    
   