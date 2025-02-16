from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import *
# from django.contrib.auth import get_user_model

# User = get_user_model()

# Create your views here.

def Header(request):
    pk = request.user.id
    user = CustomUser.objects.get(id=pk)
    useremail = user.email.split('@')[0]
    print(useremail)

    return render(request, 'header.html', {'useremail': useremail})

def LoginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        email = request.POST.get('email').lower()
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or password doesn't exit")

    context = {'page' : page}
    return render(request, 'loginRegister.html', context)

def home(request):
    return render(request, 'home.html')

def LogoutUser(request):
    logout(request)
    return redirect('login')

def RegisterPage(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip().lower()
        email = request.POST.get('email', '').strip().lower()
        password = request.POST.get('password', '')

        if CustomUser.objects.filter(email=email).exists():
            messages.info(request, 'This email is already registered!')
            return redirect('register')

        # Create user using create_user() from CustomUserManager
        user = CustomUser.objects.create_user(
                                                name=username,
                                                email=email,
                                                password=password)

        login(request, user)
        messages.success(request, 'Account created successfully!')
        return redirect('home')

    return render(request, 'loginRegister.html', {'page': 'register'})

@login_required(login_url='login')
def UpdatUser(request,id):
    updateuser = CustomUser.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST
        profile = request.FILES.get('userprofile')

        username = data.get('username')
        email = data.get('email')
        user_bio = data.get('user_bio')

        updateuser.name = username
        updateuser.email = email
        updateuser.user_bio = user_bio

        if profile:
            updateuser.user_profile = profile

        updateuser.save()
        messages.success(request, 'User account has been successfully updated!')
        return redirect('home')

    return render(request, 'update-user.html', {'user':updateuser})


# def Home(request):
#     q = request.GET.get('q') if request.GET.get('q') != None else ''

#     rooms = Room.objects.filter(
#         Q(Topic__name__icontains = q) |
#         Q(name__icontains = q) |
#         Q(description__icontains = q)
#     )

#     topics = Topic.objects.all()[0:5]
#     room_count = rooms.count()
#     room_messages = Message.objects.filter(
#         Q(room__topic__name__icontains = q)
#     )[0:3]

#     context = {
#         'rooms' : rooms,
#         'topics' : topics,
#         'room_count' : room_count,
#         'room_messages' : room_messages
#     }

#     return render(request, 'base/home.html', context)

# def Room(request, pk):
#     room = Room.objects.get(id=pk)
#     room_messages = room.message_set.all()
#     members = room.members.all()

#     if request.method == "POST":
#         messages = Message.objects.create(
#             user = request.user,
#             room = room,
#             comment = request.POST.get('comment')
#         )
#         room.members.add(request.user)
#         return redirect('room', pk=room.id)

#     context = {
#         'room' : room,
#         'room_messages' : room_messages,
#         'members' : members
#     }

#     return render(request, 'base/room.html', context)

# def UserProfile(request, pk):
#     user = CustomUser.objects.get(id = pk)
#     rooms = user.room_set.all()
#     room_messages = user.message_set.all()
#     topics = Topic.objects.all()
#     context = {
#         'user' : user,
#         'rooms' : rooms,
#         'room_messages' : room_messages,
#         'topics' : topics
#     }

#     return render(request, 'base/profile.html', context)

# @login_required(login_url='login')
# def CreatedRoom(request):
#     form = RoomForm()
#     topics = Topic.objects.all()
#     if request.method == 'POST':
#         topic_name = request.POST.get('topic')
#         topic, created = Topic.objects.get_or_create(name=topic_name)

#         Room.objects.create(
#             host = request.user,
#             topic = topic,
#             name = request.POST.get('name'),
#             description = request.POST.get('description'),
#         )
#         return redirect('home')

#     context = {
#         'form' : form,
#         'topics' : topics
#     }
#     return render(request, 'base/room_form.html', context)

# @login_required(login_url='login')
# def DeleteRoom(request, pk):
#     room = Room.objects.get(id = pk)

#     if request.user != room.host:
#         return HttpResponse('Your are not allowed here!')

#     if request.method == "POST":
#         room.delete()
#         return redirect('home')
#     return render(request, 'base/delete.html', {'delete' : room})

# @login_required(login_url='login')
# def DeleteMessage(request, pk):
#     message = Message.objects.get(id = pk)

#     if request.user != message.user:
#         return HttpResponse('Your are not allowed here!')

#     if request.method == "POST":
#         message.delete()
#         return redirect('home')

#     return render(request, 'base/delete.html', {'delete' : message})

# def TopicPage(request):
#     q = request.GET.get('q') if request.GET.get('q') != None else ''
#     topics = Topic.objects.filter(name__icontains = q)
#     return render(request, 'base/topics.html', {'topics':topics})

# def ActivityPage(request):
#     room_messages = Message.objects.all()
#     return render(request, 'base/activity.html', {'room_messages':room_messages})