from django.http import JsonResponse


def  getRoutes(request):
     
    routes  =[
        'GET /api/rooms',
        #api route that get's a room
        'GET /api/rooms/:id'
           
      ]  
    return JsonResponse(routes, safe=False)