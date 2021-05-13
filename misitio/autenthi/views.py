from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.postgres.search import SearchVector, SearchQuery, TrigramSimilarity
from django.contrib.postgres.operations import UnaccentExtension, TrigramExtension
from django.contrib import messages
from .models import *


#region Dictionary for view
lessons = [
    {'title':'Aleman-Sustantivos', 'section': 'ger_nouns', 'numbers': [
        'Lección 1: Localidades', 'Lección 2: Hogar 1',
        'Lección 3: Hogar 2', 'Lección 4: Familia',
        'Lección 5: Animales', 'Lección 6: Herramientas',
        'Lección 7: Alimentos', 'Lección 8: Vehiculos'
         ]},
    {'title':'Aleman-Verbos', 'section': 'ger_verbs', 'numbers': [
        'Lección 1: Trabajo', 'Lección 2: Comida',
        'Lección 3: Moverse', 'Lección 4: Comprar'
        ]},
    {'title':'Ingles-Weird Words', 'section': 'eng_pro', 'numbers': [
        'Lección 1: Algo 1'
        ]}
]
#endregion

# Create your views here.
def home(request):
    return render(request, "home.html", {'lessons': lessons})


def register(request):

    if request.method == 'POST':
        name = request.POST['nombre']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        to_home = False
        if password1 == password2:     
            if User.objects.filter(username=username).exists(): 
                messages.info(request, 'Username Taken')  
                username = ''
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')  
                email = ''
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=name)
                user.save()
                messages.success(request, "User created, YAY!")
                to_home = True
        else:
            messages.info(request, "Passwords doesn't match!")
            

        if to_home==True:
            return redirect('/')
        else:
            return render(request, 'register.html', {'name': name, 'username': username, 'email': email})


    else:
        return render(request, 'register.html')

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "You've log in successfully")
            return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('/login')
    else:
        return render(request, 'login.html')

def logout(request):
    messages.success(request, "You've log out successfully")
    auth.logout(request)
    return redirect('/')

