from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature
# Create your views here.
def index(request):
    '''
    name = "Patrick"
   
    context = {
        'name': 'Patrick',
        'age': 23,
        'nationality': 'British'

    }
    
    '''
    feature1 = Feature()
    feature1.id = 0
    feature1.name = "Fast"
    feature1.details = 'Our service is very quick'

    feature2 = Feature()
    feature2.id = 1
    feature2.name = "Reliable"
    feature2.details = 'Our service is very reliable'

    feature3 = Feature()
    feature3.id = 2
    feature3.name = "Affordable"
    feature3.details = 'Our service is very affordable'

    feature4 = Feature()
    feature4.id = 3
    feature4.name = "Easy to Use"
    feature4.details = 'Our service is very easy to use'
    
    return render(request, 'index.html', {'feature1': feature1, 'feature2': feature2, 'feature3': feature3, "feature4": feature4})
    
def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})