from django.shortcuts import render
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

def categories(request, slug =None):
    category = Category.objects.all()
    
    games = Game.objects.all().filter(category__slug = slug)
    
    if slug and games:
        print(request.GET.get('sort'))
        return render(request, 'games/category_slug.html', context={'category': category, "games":games})
    else:
        return render(request, 'games/category.html', context ={'category': category, "games":games})

def product(request, slug = None):
    
    games = Game.objects.all().filter(slug=slug)
    if games:
        
        return render(request, 'games/product.html', context= {'games' : games} )
    else:
        return render(request, 'games/404.html', status=404)