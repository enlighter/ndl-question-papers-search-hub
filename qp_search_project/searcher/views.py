from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'email1': "mandal.sushovan92@gmail.com"}
    return render(request, 'searcher/index.html', context_dict)