from django.db import models

# Create your models here.
class Category(models.Model):

    title = models.CharField(max_length=50, verbose_name="Category title" )
    description = models.TextField(max_length=150, verbose_name= "Category description")
    is_active = models.BooleanField(verbose_name='Category is active')
    slug = models.SlugField(unique=True, verbose_name="URL")

    class Meta:
        verbose_name ='Category'
        verbose_name_plural = 'Categories'
    
    def __str__ (self):
        return(f'{self.title}')

class Game(models.Model):

    name = models.CharField(max_length=50, verbose_name='Game Name')
    description = models.TextField(max_length=150, verbose_name='Game Description')
    is_active = models.BooleanField(verbose_name='Game is active?')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='publish date')
    release_date_at = models.DateTimeField( verbose_name='Release date')
    price = models.DecimalField(verbose_name='Game Prise', max_digits=8, decimal_places=2)
    category = models.ForeignKey(Category, verbose_name=("Game Category"), on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(unique=True, verbose_name="URL")
    game_image = models.ImageField(upload_to='images/')
    

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'

    def __str__(self):
        return (f"{self.name}")