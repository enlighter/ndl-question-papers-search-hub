from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView, CreateView

from .forms import LoginForm, RegistrationForm
from .models import student

applink = "/searcher"
#put the full weblink to forum here
forumlink = ""
boards_list = [
    'CBSE Class X',
    'CBSE Class XII',
    'JEE',
    'ICSE',
    'WBJEE',
]

def index(request):
    items_list = []
    for board in boards_list:
        dict = {
            'header': "Search past %s papers" % board,
            'link': "applink" + '/search?',
            'content': "Click here to search within %s exam question papers" % board,
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
    form_class = LoginForm


    def get_context_data(self, **kwargs):
        context = super(Login, self).get_context_data(**kwargs)
        context['applink'] = applink
        context['forumlink'] = forumlink
        return context

class Register(CreateView):
    template_name = 'searcher/register.html'
    form_class = RegistrationForm
    model = student
    success_url = '/searcher/login'

    def get_context_data(self, **kwargs):
        context = super(Register, self).get_context_data(**kwargs)
        context['applink'] = applink
        context['forumlink'] = forumlink
        return context