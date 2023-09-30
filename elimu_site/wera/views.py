from django.shortcuts import render
from . models import  Room
# importing model Room
# from  django.http import HttpResponse

# Create your views here.
def home(request,):
    teams = Room.objects.all()
    context  = {'teams':teams}
    return render(request, 'wera/home.html', context)


def room(request,pk):
    
    team  = Room.objects.get(id=pk)
    context = {'team': team}  
    return  render(request, 'wera/room.html', context)


def scores(request):
    return render(request, 'wera/scores.html', {})

def navbar(request):
    return render(request, 'wera/navbar.html',{})


# teams  = [
#     {'id':1, 'name':'NewCastle!'},
#     {'id':2, 'name':'Barcelona!'},
#     {'id': 3, 'name':'chelsea!'},
#     {'id': 4, 'name':'Manchester-Unitd'},
#     {'id':5, 'name':'Arsenal'},
#     {'id':6, 'name':'Real-Madrid'},
#     {'id':7, 'name':'Totehnam-hotspur'},
# ]