from django.urls import path
from . import views


#app url file

urlpatterns = [
    path('', views.home, name="home"),
    path('room/', views.room, name="room"),
    path('scores/', views.scores, name="scores"),
  

]

