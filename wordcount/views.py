import operator

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import HomeForm

def home(request):
    if request.method == 'POST':
        form=HomeForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/count/')
    else:
        form = HomeForm()

    return render(request, 'home.html', {'form': form})

def about(request):
    return render(request, 'about.html')

def count(request):
    fulltext = request.POST['your_text']

    wordlist = fulltext.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #Increase
            worddictionary[word] += 1
        else:
            #add to the dictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})


    