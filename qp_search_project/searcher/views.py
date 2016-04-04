from django.shortcuts import render
from django.http import HttpResponse

#from .forms import NameForm

applink = "/searcher"
#put the full weblink to forum here
forumlink = ""

def index(request):
    context_dict = {
        'applink' : applink,
        'forumlink' : forumlink
    }
    return render(request, 'searcher/index.html', context_dict)
