from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')
def password(request):

    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('Uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('Numbers'):
        characters.extend(list('9876543210'))
    if request.GET.get('Special'):
        characters.extend(list('!@#$%^&*()_+=-?><'))
    length = int(request.GET.get('length', 10))
    thepassword = ''
    if length < 15:
        for x in range(length):
            thepassword += random.choice(characters)
    else:
        thepassword = 'go fuck yourself you moron'
    return render(request, 'generator/password.html', {'password':thepassword})

def aboutme(request):
    return render(request, 'generator/aboutme.html')
