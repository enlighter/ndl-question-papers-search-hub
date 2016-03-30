from django.shortcuts import render
from django.http import HttpResponse

from .forms import NameForm

def index(request):
    context_dict = {
        'email1': "mandal.sushovan92@gmail.com",
        'form' : NameForm
    }
    return render(request, 'searcher/index.html', context_dict)