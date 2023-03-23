from django.urls import path, include, re_path

from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from .forms import CustomPasswordChangeForm
from allauth.account import views as allauth_views
app_name = 'users'

urlpatterns = [
    
    path('register/', allauth_views.SignupView.as_view(template_name = 'registration/register.html'), name = 'register'),
    path('login/', allauth_views.LoginView.as_view(template_name = 'registration/login.html'),name='login' ),
    path('logout/', allauth_views.LogoutView.as_view(),name='logout' ),
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
