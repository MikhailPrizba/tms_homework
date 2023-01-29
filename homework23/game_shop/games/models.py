from django.db import models


# Create your models here.
class ShopInfoMixin(models.Model):
    title = models.CharField(max_length=50, verbose_name="Title" )
    description = models.TextField( verbose_name= "Description")
    is_active = models.BooleanField(verbose_name='is active')
    slug = models.SlugField(unique=True, verbose_name="URL")

    class Meta:
        abstract = True
class Category(ShopInfoMixin):

    games_amount = models.IntegerField(default=0, verbose_name='amount')

    class Meta:
        verbose_name ='Category'
        verbose_name_plural = 'Categories'
    
    def __str__ (self):
        return(f'{self.title}')

class Game(ShopInfoMixin):

    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='publish date')
    release_date_at = models.DateField(verbose_name='Release date')
    price = models.DecimalField(verbose_name='Game Prise', max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, verbose_name=("Game Category"), on_delete=models.SET_NULL, null=True)
    game_image = models.ImageField(upload_to='images/')
    

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'

    def __str__(self):
        return (f"{self.title}")

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

@receiver(post_save, sender = Game)   
def create_game(instance, created,**kwargs):
    if created:
        profile = instance.category
        profile.games_amount +=1
        profile.save()

@receiver(post_delete, sender = Game)
def create_game(instance, **kwargs):
    profile = instance.category
    profile.games_amount -=1
    profile.save()