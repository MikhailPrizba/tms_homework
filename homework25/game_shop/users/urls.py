from django.urls import path, include, re_path

from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .forms import CustomPasswordChangeForm
app_name = 'users'

urlpatterns = [
    
    path('register/', views.register, name = 'register'),
    path('login/', auth_views.LoginView.as_view( next_page = 'store:index', ),name='login' ),
    path('logout/', auth_views.LogoutView.as_view( next_page = 'store:index', ),name='logout' ),
    path(
        'change-password/', 
        auth_views.PasswordChangeView.as_view(
            success_url = reverse_lazy('users:password_changed_done'),
            form_class = CustomPasswordChangeForm
            ), 
            name = "change_password" ),
    path('change-pass-done/', auth_views.PasswordChangeDoneView.as_view(), name= 'password_changed_done'),
    path('', include('django.contrib.auth.urls')),
]
