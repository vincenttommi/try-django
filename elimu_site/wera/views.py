from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from . models import  Room,Topic
from  .forms import RoomForm
from  django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import  messages
from django.contrib.auth import authenticate,login
from django.shortcuts  import  redirect
from django.contrib.auth import  logout
from django.contrib.auth.decorators import  login_required
from django.http import  HttpResponse
from django.contrib.auth.forms import  UserCreationForm

# importing model Room
# from  django.http import HttpResponse

# Create your views here.
def home(request,):
     
    q = request.GET.get('q') if request.GET.get('q') != None else ' '
    #dictionary  parameter that contains all GETparameters passed in Http request
    # request.GET.get('q) attempts to  retrieve the value of parameter from GET parameteres
    
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q)|
        Q(description__icontains=q)
    )
    #performs a database query using object-Relational Mapping  to filter Rooms based on certain conditions
      
    topics = Topic.objects.all()
    room_count   = rooms.count()
    #method to get number of rooms available intead of using  len()
    
    context  = {'rooms': rooms, 'topics':topics, 'room_count': room_count}
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


@login_required(login_url='/login')            
def createRoom(request):
    
    #restricting other users from  creating room in another admins panel
    
    if request.user != room.host:
        return HttpResponse("you are not allowed here")
    
    
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

@login_required(login_url='/login')
def  updateRoom(request,pk):

    room  = Room.objects.get(id=pk) #retrieves a specific Room object from the database using it's primary key
    form  = RoomForm(instance=room) # create  aform instance  for  the retrieved Room object (room)
    
    

    #Restricting an authorized  users from acessing the  admin DashBoard
    if request.user != room.host:
        return HttpResponse("your are not allowed  here!")
    
    
    #checking if the   data is posted and being redirected
    if request.method  == 'POST':
        form  = RoomForm(request.POST,instance=room)
        if  form.is_valid():
            form.save()
            return  redirect('home')
    
    
    
    context = {'form':form} #  a form dictionary containing it's'form' variable
    return render(request, 'wera/room_form.html', context)

@login_required(login_url='/login')
def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    
    
    
    #Restricting  user from accessing  deleting other admins  users.
    if request.user != room.host:
        return HttpResponse("your are not allowed here")
        
    
    
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'wera/delete.html',{'obj':room})




def loginP(request):
    
    page  = 'login'
    #redirecting user  to home-page after being authicated
    
    if request.user.is_authenticated:
        return redirect('home')
    
    
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username).lower()
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')
            return redirect('login')
        
        user = authenticate(request, username=username, password=password) 
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or password is incorrect')
            return redirect('login')
    
    context = {'page':page}
    return render(request, 'wera/login_register.html', context)




def logoutUser(request):
    logout(request)
    return redirect('home')
    
def registerPage(request):
    form = UserCreationForm(request.POST)
    #writing an if statement that process the form
    if request.method == 'POST':

        if form.is_valid():
            user = form.save(commit=False)
        #getting current user name and updating to lowercase()
        user.username = user.username.lower()
        user.save()
        login(request, user)
        return redirect('home')
    
    else:
        messages.error(request, 'An error occured during registration')
    
    form = UserCreationForm()
    return render(request, 'wera/login_register.html', {'form':form})       
                