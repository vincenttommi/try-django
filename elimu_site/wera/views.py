from django.shortcuts import render, redirect
from . models import  Room
from  .forms import RoomForm
# importing model Room
# from  django.http import HttpResponse

# Create your views here.
def home(request,):
    room = Room.objects.all()
    context  = {'rooms':room}
    return render(request, 'wera/home.html', context)


def room(request,pk):
    
    team  = Room.objects.get(id=pk)
    context = {'rooms': room}  
    return  render(request, 'wera/room.html', context)


def scores(request):
    return render(request, 'wera/scores.html', {})

def navbar(request):
    return render(request, 'wera/navbar.html',{})

  # Import your RoomForm if not already imported


# def  createRoom(request):
#     form =  RoomForm()
#     if request.method  == 'POST':
#         print(request.POST)
        
#         context  = {'form': form}
#         return render(request,'wera/room_form.html', context) 
            
def createRoom(request):
    # if request.method == 'POST':
    #     form = RoomForm(request.POST)
    #     request.POST.get('name')
    #     if form.is_valid():
              
    #        return HttpResponse("Form submitted successfully")
    # else:
    #     form = RoomForm()
    form  =  RoomForm()
    if  request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
            
            
        context = {'form': form}
        return render(request, 'wera/room_form.html', context)        

# rooms  = [
#     {'id':1, 'name':'NewCastle!'},
#     {'id':2, 'name':'Barcelona!'},
#     {'id': 3, 'name':'chelsea!'},
#     {'id': 4, 'name':'Manchester-Unitd'},
#     {'id':5, 'name':'Arsenal'},
#     {'id':6, 'name':'Real-Madrid'},
#     {'id':7, 'name':'Totehnam-hotspur'},
# ]