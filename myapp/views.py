from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature
from .models import Post

# Create your views here.
def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})


def form(request):
    return render(request, 'form.html')


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



def counter(request):
    text = request.POST['text']
    amount_words = len(text.split())

    posts = [1, 2, 3, 4, 5, 'tim', 'tom']
    return render(request, 'counter.html', {'posts':posts })


def blog(request):
    blogs = Post.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})

def post(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'post.html', {'post':post})