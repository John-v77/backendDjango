from django.shortcuts import render
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




