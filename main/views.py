from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


def revers(request):
    return render(request, 'main/revers.html')
