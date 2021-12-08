from django.shortcuts import render

# Create your views here.
def room(request, room_name):
    return render(request, 'mirror/room.html', {
        'room_name': room_name
    })

def test(request):
    return render(request, 'mirror/test.html')