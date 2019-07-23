from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text =  request.GET['fulltext']
    words = text.split()
    words_dictionary = {}

    want_text = request.GET['wantword']
    want_dictionary = words.count(want_text)

    for word in words:
        if word in words_dictionary:
            words_dictionary[word] += 1
        else:
            words_dictionary[word] = 1


    return render(request, 'result.html', {'full': text, 'total_words': len(words), 'dic_words' : words_dictionary.items(), 'you_want' : want_dictionary, 'want_text' : want_text})
