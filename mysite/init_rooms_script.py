from senior_des.models import Rooms

x1 = Rooms (room_name = "Justin's room", room_number = "402", is_occupied = False)
x2 = Rooms (room_name = "Matt's room", room_number = "35", is_occupied = False)
x3 = Rooms (room_name = "Nathan's room", room_number = "240", is_occupied = True)
x4 = Rooms (room_name = "Derek's room", room_number = "42", is_occupied = False)

x1.save()
x2.save()
x3.save()
x4.save()

Rooms.objects.all()

