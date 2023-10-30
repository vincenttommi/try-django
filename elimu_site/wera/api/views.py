from  rest_framework.decorators import api_view
from rest_framework.response import Response
from wera.models import Room
#importing  room from our wera models
from .serializers import RoomSerializer
from .serializers import MessageSerializer
#importing serializers that turns  python objects into json objects
from wera.api import  serializers
from  wera.models import Message

@api_view(['GET'])
def  getRoutes(request):
     
    routes  =[
        # 'GET /api/rooms',
        #api route that get's a room
        'GET /api/rooms',
        'GET /api/rooms/:id',
      # route to  get all messages
         'GET/api/messages',  
         'GET/api/messages/:id'
      ]  
    return Response(routes)
  
 #route to  get all messages 
@api_view(['GET'])
def getMessages(request):
  messages = Message.objects.all()
  #query to get all messages
  serializer  = MessageSerializer(messages, many=True)
  return Response(serializer.data)
  
  
  
@api_view(['GET'])
def getMessage(request, pk):
  # message  = Message.objects.all(pk=id)
  message  = Message.objects.get(id=pk) 
  # serializer = MessageSerializer(message, many=False)
  serializer  =  MessageSerializer(message, many=False)
  return Response(serializer.data)

  
@api_view(['GET'])  
def getRooms(request):
  rooms = Room.objects.all()
  #query to get all the rooms from  db an serialize  them into json objects
  serializer = RoomSerializer(rooms,many=True)
  return Response(serializer.data)


#api routes for getting single rooms
@api_view(['GET'])
def getRoom(request,pk):
  room  = Room.objects.get(id=pk) 
  serializer  =  RoomSerializer(room, many=False)
  #making it false so as it an return a  one room
  return Response(serializer.data)

   
