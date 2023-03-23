from rest_framework import serializers
from games.models import Game,Category

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        exclude = ('is_active', 'pub_date')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('is_active', )