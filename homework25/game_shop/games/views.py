from django.shortcuts import render, get_object_or_404, get_list_or_404
from games.models import Game, Category
from django.http import HttpResponse, HttpRequest
# Create your views here.
def index(request: HttpRequest):
    sort = request.GET.get('sort','None')
    sort_game = {
        'None': Game.objects.all(),
        'price:asc': Game.objects.all().order_by('price'),
        'price:desc': Game.objects.all().order_by('-price'),
        'name:asc': Game.objects.all().order_by('title'),
        'name:desc': Game.objects.all().order_by('-title'),
    }

    
    return render(request, 'games/home.html', context= {'games': sort_game[sort]} )

def all_categories(request: HttpRequest):
    category = Category.objects.filter(is_active = True)
    return render(request, 'games/category.html', context ={'category': category,})


def categories(request, slug):
    category = get_object_or_404(Category, slug = slug)
    games = category.game_set.filter()
    
    #games = Game.objects.all().filter(category__slug = slug)
    
    return render(request, 'games/category_slug.html', context={'category': category, "games":games})
    
    

def product(request, slug ):
    
    games = get_object_or_404(Game, slug = slug)
    
    return render(request, 'games/product.html', context= {'games' : games} )
   