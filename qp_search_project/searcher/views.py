from django.shortcuts import render
from django.http import HttpResponse

#from .forms import NameForm

applink = "/searcher"
#put the full weblink to forum here
forumlink = ""
boards_list = [
    'CBSE Class X board',
    'CBSE Class XII board',
    'JEE',
    'ICSE',
]

def index(request):
    items_list = []
    for board in boards_list:
        dict = {
            'header': "%s papers" % board,
            'link': "applink" + '/search?',
            'content': "Click here to browse all %s exam question papers" % board,
        }
        items_list.append(dict)

    context_dict = {
        'applink' : applink,
        'forumlink' : forumlink,
        'itemslist' : items_list,
    }
    return render(request, 'searcher/index.html', context_dict)
