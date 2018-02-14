from django.shortcuts import render, HttpResponse

from senior_des.models import Rooms

# Create your views here.

def room(request):
    #first see if new info needs to be put into the database
    s = request.META['QUERY_STRING']
    if (s == ''):
        print('should have no additional rooms or info')
    else:
        print(s)
        each_info = s.split('+')
        if (each_info[2] == 'false'):
            each_info[2] = False
        elif (each_info[2] == 'true'):
            each_info[2] = True
        else:
            print("WTF just happened not right")
        x = Rooms (room_name=each_info[0], room_number=each_info[1], is_occupied=bool(each_info[2]))

        #check to see if room exists or create a new room
        r = Rooms.objects.all().filter(room_name=each_info[0]).filter(room_number=each_info[1])
        #if no rooms then create new one
        if(len(r) == 0):
            x.save()
            print("Room doesn't exist")
        #if room does exist then update the state
        else:
            o = r.first()
            print("here is the room being updated: ", o)
            o.is_occupied = x.is_occupied
            o.save()

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

#def database(request):
    #add to database the request sent
