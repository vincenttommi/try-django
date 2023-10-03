from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
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

            
def createRoom(request):
    form  =  RoomForm()
    if  request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RoomForm()  #Move the  form instantiation here for GET requests    
            
            
        context = {'form': form}
        return render(request, 'wera/room_form.html', context) #used to render the template       
