from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='shop'),
    
    path('categories/', views.all_categories, name='categories'),
    path('categories/<slug:slug>/', views.categories, name='slug_categories'),
    path('product/', views.product, name='product'),
    path('product/<slug:slug>/', views.product, name='product'),
    path('form/', views.form_practice, name='forms'),
    path('<slug:game_slug>/comment/', views.CommentCreateView.as_view(), name='comment-add'),
    path('comment/<int:pk>/update', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
]
