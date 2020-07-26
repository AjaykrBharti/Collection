from django.shortcuts import render
from django.http import HttpResponse
from random_word import RandomWords
from PyDictionary import PyDictionary


# Create your views here.
def index(request):


    singleword = 'hello'
    defination = ''
    translate = ''
    keys = ''
    values = ''
    word = ''
    if 'getword'in request.POST:
        r = RandomWords()
        dictionary = PyDictionary()
        word = r.get_random_word(hasDictionaryDef="true")
        wordone = word.replace('a','_')
        wordtwo = wordone.replace('e','_')
        wordthree = wordtwo.replace('i','_')
        singleword = wordthree.replace('o','_')

        try:
            defination = (dictionary.meaning(word))
            values = defination.values()
        except:
            values = ''

        print(word)
        data = request.POST
        text = data['word']

        print(text)
        if word == text:
            print('Hello')

    context = {'word': singleword,'defination':defination,'translate':translate,'values':values,'w':word}
    return render(request,'wordgame/game.html',context)