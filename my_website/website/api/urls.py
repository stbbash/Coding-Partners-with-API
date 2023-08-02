from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.getRoutes),
    path('mymembers/', views.getMembers),
    path('mymembers/<str:pk>/', views.getMember)
]


urlpatterns = format_suffix_patterns(urlpatterns)