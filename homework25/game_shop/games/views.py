from django.shortcuts import render, get_object_or_404, get_list_or_404
from games.models import Game, Category, Comment
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
#from games.forms import GameSearchForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
# Create your views here.

class CommentCreateView(CreateView):
    model = Comment
    fields = ['text','rating']

    def form_valid(self, form) -> HttpResponse:
        form.instance.game = Game.objects.get(slug = self.kwargs['product_slug'])
        return super().form_valid(form)
class CommentUpdateView(UpdateView):
    model = Comment
    fields = ['text','rating']

class CommentDeleteView(DeleteView):
    model = Comment
    def get_success_url(self, **kwargs) -> str:
        return reverse_lazy('store:product', kwargs = {'product_slug': self.get_object().game.slug})


def index(request: HttpRequest):
    sort = request.GET.get('sort','None')
    sort_game = {
        'None': Game.objects.all(),
        'price:asc': Game.objects.all().order_by('price'),
        'price:desc': Game.objects.all().order_by('-price'),
        'name:asc': Game.objects.all().order_by('title'),
        'name:desc': Game.objects.all().order_by('-title'),
    }
    
    return render(request, 'games/home.html', context= {'games': sort_game[sort], },  )

def all_categories(request: HttpRequest):
    category = Category.objects.filter(is_active = True)
    return render(request, 'games/category.html', context ={'category': category,})


def categories(request, slug):
    category = get_object_or_404(Category, slug = slug)
    games = category.game_set.filter()
    
    #games = Game.objects.all().filter(category__slug = slug)
    
    return render(request, 'games/category_slug.html', context={'category': category, "games":games})
    
    

def product(request, product_slug ):
    
    games = get_object_or_404(Game, slug = product_slug)
    comments = games.comment_set.all()
    rating = Comment.objects.all()
    average_rating = 0
    if rating:
        for rat in rating:
            average_rating += rat.rating
        average_rating = average_rating/len(rating)
    return render(request, 'games/product.html', context= {'games' : games, 'comments':comments, 'average_rating': f"{average_rating: .2f}"}, )


class Search(ListView):

    template_name = 'games/home.html'
    context_object_name = 'games'
    
    def get_queryset(self) :
        game = Game.objects.filter(title__icontains = self.request.GET.get('q'))
        
        return game
        
    
    def get_context_data(self,*, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context
  