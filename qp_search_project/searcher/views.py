from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView

from .forms import UserLogin

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


class Login(FormView):
    template_name = 'searcher/login.html'
    form_class = UserLogin


    def get_context_data(self, **kwargs):
        context = super(Login, self).get_context_data(**kwargs)
        context['applink'] = applink
        context['forumlink'] = forumlink
        return context