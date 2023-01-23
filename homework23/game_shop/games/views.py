from django.shortcuts import render
from games.models import Game, Category
from django.http import HttpResponse, HttpRequest
# Create your views here.
def index(request):
    games = Game.objects.all()
    return render(request, 'games/home.html', context= {'games' : games} )

def categories(request, slug =None):
    category = Category.objects.all()
    
    games = Game.objects.all().filter(category__slug = slug)
    
    if slug and games:
        return render(request, 'games/category_slug.html', context={'category': category, "games":games})
    else:
        return render(request, 'games/category.html', context ={'category': category, "games":games})