from django.urls import path
from . import views


#app url file

urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('scores/', views.scores, name="scores"),
    path('navbar/', views.navbar,name="navbar" ),
  

]

