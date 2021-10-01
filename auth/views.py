from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def userHome(request):
    return render(request, 'userIndex.html')
    