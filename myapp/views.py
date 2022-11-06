from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.
def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})


def form(request):
    return render(request, 'form.html')


def counter(request):
    text = request.POST['text']
    amount_words = len(text.split())
    return render(request, 'counter.html', {'amount':amount_words})


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
    return render(request, 'login.html')





