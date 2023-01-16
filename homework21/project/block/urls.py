from django.urls import path
from . import views

urlpatterns = [
    path('class-home/', views.MyClassBasedView.as_view(), name='home'),
    path('class-home/<num>/', views.MyClassBasedView.as_view(), name='home'),
    path('factorial/', views.index, name='index')
]
