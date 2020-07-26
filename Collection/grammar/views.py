from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def index(request):


    if request.method =='POST':
        data = request.POST
        #text = data.get('Textarea1')
        text = data['Textarea1']
        print(text)

        stop_words = set(stopwords.words('english'))

        text = data['Textarea1']

        # sent_tokenize is one of instances of
        # PunktSentenceTokenizer from the nltk.tokenize.punkt module

        tokenized = sent_tokenize(text)
        for i in tokenized:
            # Word tokenizers is used to find the words
            # and punctuation in a string
            wordsList = nltk.word_tokenize(i)

            # removing stop words from wordList
            wordsList = [w for w in wordsList if not w in stop_words]

            # Using a Tagger. Which is part-of-speech
            # tagger or POS-tagger.

            tagged = nltk.pos_tag(wordsList)

            print(tagged)

            context = {'text':tagged}

    return render(request,'grammar/grammar.html',context)



