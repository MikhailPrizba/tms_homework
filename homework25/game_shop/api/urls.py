from django.urls import path

from . import views

urlpatterns = [
    path('games/', views.GetGameInfoView.as_view(), ),
    path('search-games/', views.GetGameInfoSearchView.as_view(), ),
    path('order/', views.GetGameInfoOrderView.as_view(),)
]
