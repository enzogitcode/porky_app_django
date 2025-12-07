from django.urls import path
from . import views

app_name='pigs'

urlpatterns = [
    
    #path('', views.Home.as_view(), name='home')
    path('', views.home, name='home' ),
    path('about', views.about, name='about')
]
