from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm

# rooms = [
#     {'id':1, 'name':'Lets learn python'},
#     {'id':2, 'name':'Design with me'},
#     {'id':3, 'name':'Frontend developer'},
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render (request, 'reviewapp/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    # for i in rooms:
    #     if i['id'] == int(pk):
    #         room = i 
    context = {'room':room}
    return render (request, 'reviewapp/room.html', context)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        # print(request.POST)
        # this is how we can process the data manually
        # request.POST.get('name')
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request, 'reviewapp/room_form.html', context)



def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request, 'reviewapp/room_form.html', context)


def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj':room})
