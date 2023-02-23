from django.urls import path, include, re_path

from . import views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    
    path('register/', views.register, name = 'register'),
    path('login/', auth_views.LoginView.as_view( next_page = 'store:index', ),name='login' ),
    path('logout/', auth_views.LogoutView.as_view( next_page = 'store:index', ),name='logout' ),
    path('', include('django.contrib.auth.urls')),
]
