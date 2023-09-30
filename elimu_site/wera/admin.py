from django.contrib import admin

# Register models  into our admin panel
from .models import Room,Topic,Message

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)