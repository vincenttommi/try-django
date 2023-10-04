from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from . models import  Room,Topic
from  .forms import RoomForm

# importing model Room
# from  django.http import HttpResponse

# Create your views here.
def home(request,):
    rooms = Room.objects.all()
    
    topics = Topic.objects.all()
    
    context  = {'rooms': rooms, 'topics':topics}
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



#In summary, this view function is used to display a form for updating
# a specific Room object. It retrieves the existing room data, 
# creates a form instance pre-filled with that data, 
# and renders a template to display the form to the user for editing and updating.
def  updateRoom(request,pk):

    room  = Room.objects.get(id=pk) #retrieves a specific Room object from the database using it's primary key
    form  = RoomForm(instance=room) # create  aform instance  for  the retrieved Room object (room)
    
    #checking if the   data is posted and being redirected
    if request.method  == 'POST':
        form  = RoomForm(request.POST,instance=room)
        if  form.is_valid():
            form.save()
            return  redirect('home')
    
    
    
    context = {'form':form} #  a form dictionary containing it's'form' variable
    return render(request, 'wera/room_form.html', context)


def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'wera/delete.html',{'obj':room})