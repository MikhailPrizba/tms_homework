from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework.generics import ListAPIView
import random
from games.models import Game
from .serializers import GameSerializer

#from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer


# Create your views here.
class GetGameInfoView(ListAPIView):
 #   renderre_classes = [BrowsableAPIRendere, JSONRebder]
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    def get_queryset(self):
        random_activation = self.request.query_params.get('random', None)
        if random_activation == 'true':
            return Game.objects.all().filter(id = random.randint(1, len(Game.objects.all())))
        else:
            return Game.objects.all()
