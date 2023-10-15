from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def achievement(request):
    return render(request, 'achievement.html')

def helpline(request):
    return render(request, 'helpline.html')

def donation(request):
    return render(request, 'donation.html')
