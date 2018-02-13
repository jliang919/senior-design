from django.shortcuts import render, HttpResponse

from senior_des.models import Rooms

# Create your views here.

def room(request):
    rooms = Rooms.objects.all()
    for room in rooms:
        #print(room);
        room.text = room
        #print(room.text)    
    #print(rooms)

    args = {'rooms' : rooms }
    return render(request, 'senior_des/room.html', args) 
    
def home(request):
    return render(request, 'senior_des/homepage/startbootstrap-agency-master/index.html')

