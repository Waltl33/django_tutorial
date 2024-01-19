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

# def register(request):
#     if request.method == 'POST':

#         # Check if the required fields are not empty
#         if not request.POST.get("username") or not request.POST.get("email") or not request.POST.get("password") or not request.POST.get("password2"):
#             messages.info(request, "Please fill in all the fields")
#             return redirect('register')

#         username = request.POST["username"]
#         email = request.POST["email"]
#         password = request.POST["password"]
#         password2 = request.POST["password2"]

#         if password == password2:
#             if User.objects.filter(email=email).exists():
#                 messages.info(request, 'Email Already Used')
#                 return redirect('register')
#             elif User.objects.filter(username=username).exists():
#                 messages.info(request, 'Username Already Used')
#                 return redirect('register')
#             else:
#                 try:
#                     # Create a new user
#                     user = User.objects.create_user(username=username, email=email, password=password)
#                     user.save()
#                     messages.success(request, "Registration Successful")
#                     return redirect('login')
#                 except Exception as e:
#                     messages.error(request, f"An error occurred: {e}")
#                     return redirect('register')
#         else:
#             messages.info(request, "Password Not The Same")
#             return redirect('register')
        
#     else:
#         return render(request, 'register.html')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect(register)
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect(register)
            else:
                user = User.objects.create_user(username=username, password=password,)
                user.save()
                
                return redirect('login')


        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(register)
            

    else:
        return render(request, 'register.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')
