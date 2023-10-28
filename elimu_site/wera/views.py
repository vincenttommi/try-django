from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
from . models import  Room,Topic, Message
from  .forms import RoomForm,UserForm
#importing default forms from django models
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
      
    topics = Topic.objects.all()[0:5]
    #limitting topics by  slicing to view only  five on the side-bar
    room_count   = rooms.count()
    #method to get number of rooms available intead of using  len()
    
    
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))
    
    context  = {'rooms': rooms, 'topics':topics, 'room_count': room_count,'room_messages':room_messages}
    return render(request, 'wera/home.html', context)


def room(request,pk):
    
    room  = Room.objects.get(id=pk)
    #giving  the set of message that are related to  this room
    room_messages = room.message_set.all().order_by('-created')
    participants = room.participants.all()
    #getting all the participants related with this room and passing them into context dictionary
    
    
    #posting the messages that user has  submitted via the form
    if request.method  == 'POST':
        message = Message.objects.create(
            user = request.user,
            room = room,
            body = request.POST.get('body')
            
        )    
        #before redirecting we are adding  adding participants to a user
        room.participants.add(request.user)
        return  redirect('room', pk=room.id)
    context = {'room': room,'room_messages':room_messages,'participants':participants}  
    return  render(request, 'wera/room.html', context)

  # Import your RoomForm if not already imported


# @login_required(login_url='/login')            
# def createRoom(request):
# ## Fetch the relevant room based on user (adjust this based on your model structure)    
#     try:
#         room = Room.objects.get(host=request.user)
#     except Room.DoesNotExist:
#         return HttpResponse("you are not allowed to created a room here") 
#     #checking if  request method is == POST and granting it permission to POST
#     if request.method  == 'POST':
#         form = RoomForm(request.POST)
        
#         #checking if form is valid
#         if form.is_valid():
#             form.save()
#             return redirect('home') 
#         else:
#             form  = RoomForm
            
#         context ={'form':form}
#         return render(request, 'wera/room_form.html', context) 

@login_required(login_url='/login')
def createRoom(request):
    form  =  RoomForm()
    
    #query to get topics from  db
    topics = Topic.objects.all()
    
    #checking it request message  == POST
    if request.method  == 'POST':
        
        #getting the topic name from db
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        #if the method is not existing get would create it and if exist , it returns itc
        
        Room.objects.create(
            
            host  = request.user,
            topic=topic,
            #find the topic  in database or the newly created
            name=request.POST.get('name'),
            description=request.POST.get('description')
            #getting description from the frontend
            
        )
      
        return redirect('home')
            

    context = {'form': form, 'topics':topics}
    return render(request, 'wera/room_form.html', context)




#In summary, this view function is used to display a form for updating
# a specific Room object. It retrieves the existing room data, 
# creates a form instance pre-filled with that data, 
# and renders a template to display the form to the user for editing and updating.

@login_required(login_url='/login')
def  updateRoom(request, pk):
    room  = Room.objects.get(id=pk) #retrieves a specific Room object from the database using it's primary key
    form  = RoomForm(instance=room) # create  aform instance  for  the retrieved Room object (room)
    #query to get topics from  db
    topics = Topic.objects.all()
    #Restricting an authorized  users from acessing the  admin DashBoard
    if request.user != room.host:
        return HttpResponse("your are not allowed  here!")
    #checking if the   data is posted and being redirected
    if request.method  == 'POST':
        
        # query to get  all topics from db
        topics_name = request.POST.get('topic')
        topic, created  = Topic.objects.get_or_create(name=topics_name)
        #if the method is not existing get would create it and if exist , it returns it
        #
        room.name = request.POST.get('name')
        #query to get the name of the room
        room.topic  = topic
        #getting topic of newly created or edited by the user
        room.description = request.POST.get('description')
        room.save()
        return  redirect('home')

    context = {'form':form, 'topics':topics, 'room':room } #  a form dictionary containing it's'form' variable
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
    #redirects the user back to homepage after deleting the page
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
            user = User.objects.get(username=username)
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
    form = UserCreationForm()
    user = None  # Initialize the user variable

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # Getting the current username and updating to lowercase()
            user.username = user.username.lower()
            user.save()
            login(request, user)    
            return redirect('home')
        else:
            # Handle the case where the form is not valid
            # For example, you can display an error message or redirect to a registration error page
            return HttpResponse("Registration failed. Please check the form.")
    else:
        messages.error(request, 'An error occurred during registration')

    return render(request, 'wera/login_register.html', {'form': form})    



#function for User deleting the Message
@login_required(login_url='login')
def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)
    
    #checking if  is eqaul to the correct host
    if  request.user != message.user:
        return HttpResponse("your are not  allowed he")
    
    
    #checking if the method is post before posting the data
    if request.method  == 'POST':
        #deletes the message
        message.delete()
        return redirect('home')
    #redirects the user back to homepage after deleting the page
    return render(request, 'wera/delete.html',{'obj':message})
    
    
    
    


#funcion to check user profile
def  userProfile(request,pk):
    user  =  User.objects.get(id=pk)
    # an object that recieves   primary keys from  default User
    
    #getting all user rooms
    rooms  =  user.room_set.all()  
    room_messages = user.message_set.all()
    #getting all  room_messages
    topics  =  Topic.objects.all()
    #getting all the user topics from db
    
    
    context = {'user':user, 'rooms':rooms,'room_messages':room_messages,'topics':topics }
    return render(request, 'wera/profile.html', context)




#function based view for updating user
@login_required(login_url='login')
def updateUser(request):
    
    user = request.user
    #query to get data of the user from form
    form = UserForm(instance=request.user)
    #creating instance of user created  from  default forms
    
    #condition for chekcking  incoming is post before posting the instance
    if request.method  == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return redirect('user-profile', pk=user.id)
            
    
    return render(request, 'wera/update-user.html',{'form':form})


#function based for handling out topics
def  topicsPage(request):
    q = request.GET.get('q')if request.GET.get('q') != None else ''
    #sending the request to topics to return them  when searching
    topics  = Topic.objects.filter(name__icontains=q)
    #query to filter  topics from db 
    
    return render(request, 'wera/topics.html', {'topics':topics})




#Creating a function to render handle functions of activity
def  activityPage(request):
    
    room_messags =  Message.objects.all()
    #query to get all messages of various rooms
    
    
    return render(request, 'wera/activity.html', {'room_messages':room_messags})
