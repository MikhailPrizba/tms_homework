from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework.generics import ListAPIView
import random
from games.models import Game
from .serializers import GameSerializer
from rest_framework.pagination import PageNumberPagination

from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework import filters as rest_filters

# Create your views here.

class ResultsSetPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 5 
class GetGameInfoView(ListAPIView):
    #renderer_classes = [BrowsableAPIRendere, JSONRebder]
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    pagination_class = ResultsSetPagination

    def get_queryset(self):
        random_activation = self.request.query_params.get('random', None)
        if random_activation == 'true':
            return Game.objects.all().filter(id = random.randint(1, len(Game.objects.all())))
        else:
            return Game.objects.all()

class GetGameInfoSearchView(ListAPIView):
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    pagination_class = ResultsSetPagination
    filter_backends = [rest_filters.SearchFilter,]
    search_fields = ['title',]

class GetGameInfoOrderView(ListAPIView):
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    pagination_class = ResultsSetPagination
    filter_backends = [rest_filters.OrderingFilter]
    ordering_fields = ['title','price','release_date_at']