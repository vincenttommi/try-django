from  django.contrib import  admin
from django.urls import path, include


#projects url
urlpatterns = [
    path('admin/',admin.site.urls),
    path('', include('wera.urls')) #adding app url to match with project url
]
