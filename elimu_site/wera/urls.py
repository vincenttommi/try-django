from django.urls import path
from . import views


#app url file

urlpatterns = [
    path('', views.home, name="home"),
    path('room/<str:pk>/', views.room, name="room"),
    path('scores/', views.scores, name="scores"),
    path('navbar/', views.navbar,name="navbar" ),
    path('create-room/',views.createRoom, name="create-room"),
    path('update-room/<str:pk>/', views.updateRoom, name = "update-room"),
    path('delete-room/<str:pk>/', views.deleteRoom, name= "delete-room")

]

