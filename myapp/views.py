from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'name': 'John',
        'profesion': 'web dev'
    }
    return render(request, 'index.html', context)