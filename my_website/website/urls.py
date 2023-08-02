from django.urls import path
from . import views

urlpatterns = [
    path('website/', views.website, name='website'),
    path('website/details/<slug:slug>/', views.details, name='details'),
    path('', views.main, name='main'),
]