from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from games.models import Game, Category

@receiver(post_save, sender = Game)   
def create_game(instance, created,**kwargs):
    if created:
        profile = instance.category
        profile.games_amount +=1
        profile.save()

@receiver(post_delete, sender = Game)
def delete_game(instance, **kwargs):
    profile = instance.category
    profile.games_amount -=1
    profile.save()