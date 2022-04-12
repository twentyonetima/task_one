from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


def vice_versa(request):
    return render(request, 'main/vice_versa.html')


def reverse(request):
    user_text = request.GET['usertext']
    reversed_text = user_text[::-1]
    return render(request, 'main/reverse.html', {'usertext': user_text, 'reversedtext':reversed_text})
