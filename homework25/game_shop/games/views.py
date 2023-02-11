from django.shortcuts import render, get_object_or_404, get_list_or_404
from games.models import Game, Category, Comment
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from games.forms import GameSearchForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# Create your views here.

class CommentCreateView(CreateView):
    model = Comment
    template_name = 'games/comment_create.html'
    fields = ['text','rating']

class CommentUpdateView(UpdateView):
    model = Comment
    template_name = 'games/comment_delete.html'
    fields = ['text','rating']

class CommentDeleteView(DeleteView):
    model = Comment
    success_url = reverse_lazy('store:index')


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

def form_practice(request: HttpRequest):
    if request.method == 'POST':
        form = GameSearchForm(request.POST)
        if form.is_valid():
            
            return HttpResponseRedirect('/thanks')
    else:
        form =GameSearchForm()
    return render(request, 'games/form.html', {'form': form})