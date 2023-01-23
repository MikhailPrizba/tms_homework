from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='shop'),
    path('categories/', views.categories, name='categories'),
    path('categories/<slug:slug>/', views.categories, name='categories'),
]
