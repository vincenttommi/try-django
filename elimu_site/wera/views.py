from django.shortcuts import render
# from  django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'wera/home.html',{})


def room(request):
    return  render(request, 'wera/room.html', {})

def scores(request):
    return render(request, 'wera/scores.html', {})


