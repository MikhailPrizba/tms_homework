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
import datetime
# Create your views here.

class CommentCreateView(CreateView): #создание комментариев
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
    games = Game.objects.all()
    if sort != 'None' :
        games = Game.objects.all().order_by(sort)

    
    return render(request, 'games/home.html', context= {'games': games, },  )

def all_categories(request: HttpRequest):
    category = Category.objects.filter(is_active = True)
    return render(request, 'games/category.html', context ={'category': category,})

@login_required
def categories(request, slug):
    category = get_object_or_404(Category, slug = slug)
    games = category.game_set.filter()
    sort = request.GET.get('sort','None')
    
    if sort != 'None' :
        games = Game.objects.all().order_by(sort)
    
    #games = Game.objects.all().filter(category__slug = slug)
    
    return render(request, 'games/category_slug.html', context={'category': category, "games":games})
    
    

def product(request, product_slug ):
    
    games = get_object_or_404(Game, slug = product_slug)
    last_visited_name = f'{request.user.username}_{product_slug}'
    last_count_name = f'{request.user.username}_{product_slug}_count'
    last_visited = request.COOKIES.get(last_visited_name)
    last_count = request.COOKIES.get(last_count_name) or 0
   
    
    comments = games.comment_set.all()
    average_rating = comments.aggregate(Avg('rating'))
    comments_count = 0

    if request.user.is_authenticated:
        first_comment = list(comments.filter(user=request.user))
        other_comments = list(comments.exclude(user=request.user))
        comments = first_comment + other_comments
        comments_count = len(request.user.comment_set.all().filter(game__slug= product_slug))
           
    
    context = {'games' : games, 
               'comments':comments, 
               'average_rating': f"{average_rating['rating__avg']}",
               'comments_count': comments_count,
               'last_visited' : last_visited,
               'last_count' : last_count
               }
    response = render(request, 'games/product.html', context )
    if request.user.is_authenticated:
        visit_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        response.set_cookie(last_visited_name, visit_time, max_age= datetime.timedelta(days=30), )
        response.set_cookie(last_count_name, int(last_count) +1, max_age= datetime.timedelta(days=30), )
    return response


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
    def render_to_response(self, context, **response_kwargs):
        print(Search.get_queryset(self))
        if not Search.get_queryset(self):
            
            return redirect('store:index')
        else:
            return super().render_to_response(context, **response_kwargs)
    
  