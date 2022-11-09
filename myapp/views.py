from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature, Post, Room, Message 
from django.http import HttpResponse
import json
import urllib.request


# Create your views here.



#first page - form page
def form(request):
    return render(request, 'form.html')

def counter(request):
    text = request.POST['text']
    amount_words = len(text.split())

    posts = [1, 2, 3, 4, 5, 'tim', 'tom']
    return render(request, 'counter.html', {'posts':posts })



# Dynamic Data - Models - Query Database. 
def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})

# Authentication - 
def register(request):
    if request.method != 'POST':
        return render(request, 'register.html')

    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']

    if password != password2:
        messages.info(request, 'Password is not the same')
        return redirect('register')

    if User.objects.filter(username=username).exists():
        messages.info(request, 'Username Already Used')
        return redirect('register')
    
    if User.objects.filter(email=email).exists():
        messages.info(request, 'Email Already Used')
        return redirect('register')
    
    user = User.objects.create_user(username=username, email=email, password=password)
    user.save()
    return redirect('login')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')

    return render(request, 'login.html')



def logout(request):
    auth.logout(request)
    return redirect('/')






# Blog page - App
def blog(request):
    blogs = Post.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})

def post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'post.html', {'post':post})


# Stock Market page - Api app
def stockMarket(request):
    if request.method != 'POST':
        stockSymbol = ''
        data={}

    else:
        stockSymbol = request.POST['stockSearched']

        # api - call
        key1 = 'pk_c7b814fba9a24e41968fa5eb41f9a1d3'
        api_link = 'https://cloud.iexapis.com/stable/stock/'+ stockSymbol +'/quote?token=' + key1

        
        
        res = urllib.request.urlopen(api_link).read()
        json_data = json.loads(res)
        data = str(json_data)
        
        data = {
            "name":str(json_data['companyName']),
            "symbol":str(json_data['symbol']),
            "week52High":str(json_data['week52High']),
            "week52Low":str(json_data['week52Low']),
            "ytdChange":str(round((json_data['ytdChange']*100), 2)),
            "todayChange":str(json_data['change']),
            "todayChangePercent":str(round((json_data['changePercent']*100), 2)),
            "latestPrice":str(json_data['latestPrice']),
        }
    return render(request, 'stock-market.html', {'data': data})


# Chat app
def chat(request):
    return render(request, 'chat.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room' : room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists(): 
         return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')