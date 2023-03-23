from django.urls import path
from . import views
app_name = 'store'
urlpatterns = [
    path('',views.index, name='index'),
    path('search/', views.Search.as_view(), name = 'search'),
    path('categories/', views.all_categories, name='categories'),
    path('categories/<slug:slug>/', views.categories, name='slug_categories'),
    #path('product/', views.product, name='products'),
    path('product/<slug:product_slug>/', views.product, name='product'),
    #path('form/', views.form_practice, name='forms'),
    path('<slug:product_slug>/comment/', views.CommentCreateView.as_view(), name='comment-add'),
    path('comment/<int:pk>/update', views.CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment-delete'),
   
]
