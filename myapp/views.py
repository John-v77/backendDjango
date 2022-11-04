from django.shortcuts import render
from .models import Feature

# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'fast'
    feature1.is_true = True
    feature1.details ="Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis numquam animi magni iure, id, soluta amet deleniti suscipit, non cupiditate quos."
    
    feature2 = Feature()
    feature2.id = 0
    feature2.name = 'fast'
    feature2.is_true = False
    feature2.details ="Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis numquam animi magni iure, id, soluta amet deleniti suscipit, non cupiditate quos."
    
    feature3 = Feature()
    feature3.id = 0
    feature3.name = 'fast'
    feature3.is_true = True
    feature3.details ="Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis numquam animi magni iure, id, soluta amet deleniti suscipit, non cupiditate quos."
    
    feature4 = Feature()
    feature4.id = 0
    feature4.name = 'fast'
    feature4.is_true = True
    feature4.details ="Lorem ipsum dolor sit amet consectetur adipisicing elit. Corporis numquam animi magni iure, id, soluta amet deleniti suscipit, non cupiditate quos."
    
    features =  [feature1, feature2, feature3, feature4]
    
    return render(request, 'models.html', {'features': features})



def counter(request):
    text = request.POST['text']
    amount_words = len(text.split())
    return render(request, 'counter.html', {'amount':amount_words})