from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


def vice_versa(request):
    return render(request, 'main/vice_versa.html')


def reverse(request):
    user_text = request.GET['usertext']
    words = user_text.split()
    number_of_words = len(words)
    reversed_text = user_text[::-1]
    if number_of_words == 1:
        answer = 'word'
    else:
        answer = 'words'
    return render(request, 'main/reverse.html', {'usertext': user_text,
                                                 'reversedtext': reversed_text,
                                                 'numberofwords': number_of_words,
                                                 'answerwords': answer
                                                 })
