from django.urls import path
from . import views

urlpatterns = [  
    path('rules/', views.rules),
    path('about/', views.about),
]  