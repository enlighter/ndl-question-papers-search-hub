from django.shortcuts import render
from django.http import HttpResponse

from .forms import NameForm

applink = "/searcher"

def index(request):
    context_dict = {
        'applink' : applink
    }
    return render(request, 'searcher/index.html', context_dict)