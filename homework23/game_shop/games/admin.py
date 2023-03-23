from django.contrib import admin
from games.models import Category, Game
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    ...