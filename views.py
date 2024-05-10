from django.shortcuts import render
from .models import Destination
# Create your views here.
def index(request):

    dest1 = Destination()
    dest1.name = 'Philippines'
    dest1.img = 'destination_1.jpg'
    dest1.desc = 'a fun place'
    dest1.price = 500
    dest1.offer = False

    dest2 = Destination()
    dest2.name = 'Malaysia'
    dest2.img = 'destination_2.jpg'
    dest2.desc = 'Malay mo, Malay niya, Malaysia'
    dest2.price = 500
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'America'
    dest3.img = 'destination_3.jpg'
    dest3.desc = 'a greasy place'
    dest3.price = 500
    dest3.offer = False

    dests = [dest1, dest2, dest3] 
    return render(request, 'index.html', {'dests': dests})