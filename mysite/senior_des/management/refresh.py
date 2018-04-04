from django.core.management.base import BaseCommand, CommandError
from polls.models import Question as Poll
from senior_des.models import Rooms

class Command(BaseCommand):

    def refresh_page(self):
        for room in Rooms.objects.all():
            room.delete()

