from django.shortcuts import render, get_object_or_404, get_list_or_404,redirect
from games.models import Game, Category, Comment
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
#from games.forms import GameSearchForm
from django.urls import reverse_lazy,reverse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.db.models import Avg
from django.contrib.auth.decorators import login_required
# Create your views here.

class CommentCreateView(CreateView):
    model = Comment
    fields = ['text','rating']

    def form_valid(self, form) -> HttpResponse:
        form.instance.game = Game.objects.get(slug = self.kwargs['product_slug'])
        form.instance.user = User.objects.get(id = self.request.user.id)
        
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
    sort_games = {
        'None': Game.objects.all(),
        'price:asc': Game.objects.all().order_by('price'),
        'price:desc': Game.objects.all().order_by('-price'),
        'name:asc': Game.objects.all().order_by('title'),
        'name:desc': Game.objects.all().order_by('-title'),
    }
    sort_game = sort_games.get(sort)
    if not sort_game:
        sort_game = Game.objects.all()
    return render(request, 'games/home.html', context= {'games': sort_game, },  )

def all_categories(request: HttpRequest):
    category = Category.objects.filter(is_active = True)
    return render(request, 'games/category.html', context ={'category': category,})

@login_required
def categories(request, slug):
    category = get_object_or_404(Category, slug = slug)
    games = category.game_set.filter()
    
    #games = Game.objects.all().filter(category__slug = slug)
    
    return render(request, 'games/category_slug.html', context={'category': category, "games":games})
    
    

def product(request, product_slug ):
    
    games = get_object_or_404(Game, slug = product_slug)
    comments = games.comment_set.all()
    average_rating = comments.aggregate(Avg('rating'))
    comments_count = 0

    if request.user.is_authenticated:
        first_comment = list(comments.filter(user=request.user))
        other_comments = list(comments.exclude(user=request.user))
        comments = first_comment + other_comments
        comments_count = len(request.user.comment_set.all())
        print(comments_count)    
    
    context = {'games' : games, 
               'comments':comments, 
               'average_rating': f"{average_rating['rating__avg']: .2f}",
               'comments_count': comments_count
               }
    
    return render(request, 'games/product.html', context )


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
    
  