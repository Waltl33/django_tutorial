from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
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
 
    features = Feature.objects.all
    
    return render(request, 'index.html', {'features': features})
    
def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})

def register(request):
    if request.method == 'POST':

        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('register')
        else:
            messages.info(request, "Password Not The Same")
            return redirect('register')
        
    else:
        return render(request, 'register.html')