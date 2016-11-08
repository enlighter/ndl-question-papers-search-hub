from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.views.generic import FormView, CreateView
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters

from .forms import RegistrationForm
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
    form_class = AuthenticationForm
    success_url = '/searcher/'

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Sets a test cookie to make sure the user has cookies enabled
        request.session.set_test_cookie()

        return super(Login, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        auth_login(self.request, form.get_user())

        # If the test cookie worked, go ahead and
        # delete it since its no longer needed
        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()

        return super(Login, self).form_valid(form)

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