from django.shortcuts import render
def map(request):
    return render(request,'imgmap.html')

def highway(request):
    return render(request,'nh.html')

def icecream(request):
    return render(request,'arunice.html')

def dominos(request):
    return render(request, 'dominos.html')

def saravana(request):
    return render(request, 'saravana.html')

def apple(request):
    return render(request, 'apple.html')
# Create your views here.
