from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse


# Create your models here.
class ShopInfoMixin(models.Model):
    title = models.CharField(max_length=50, verbose_name="Title" )# как преопределить значение verbose_name  чтобы можно было
    description = RichTextField( verbose_name= "Description")# написать типо Game Title, Game Descriptions
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
        indexes = [
            models.Index(fields=['title']) # создание индекса по title
        ]

    def __str__(self):
        return (f"{self.title}")

class Comment(models.Model):
    text = models.TextField(max_length=150, verbose_name='Comment text')
    pub_date = models.DateField(verbose_name='Comment publication date', auto_now_add=True, editable=False)
    rating = models.IntegerField(verbose_name='Comment rating',  )
    game = models.ForeignKey(Game, verbose_name='Game', on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("store:product", kwargs={"game_slug": self.game.slug})
    