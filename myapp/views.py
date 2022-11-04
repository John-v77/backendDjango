from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'name': 'John',
        'profesion': 'web dev'
    }
    return render(request, 'form.html')



def counter(request):
    text = request.POST['text']
    amount_words = len(text.split())
    return render(request, 'counter.html', {'amount':amount_words})