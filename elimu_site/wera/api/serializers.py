from rest_framework.serializers import  ModelSerializer
from  wera.models  import Room
from wera.models import Message


#import details of the room and turning them back to json object
class  RoomSerializer(ModelSerializer):
    class  Meta:
        model = Room
        fields  = '__all__'


class MessageSerializer(ModelSerializer):
    class Meta:
        model  = Message
        fields  = '__all__'
        
