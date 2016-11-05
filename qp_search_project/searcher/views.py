from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm

from .forms import LoginForm, RegistrationForm

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


class Register(FormView):
    template_name = 'searcher/register.html'
    #form_class = RegistrationForm

    def get_context_data(self, *args, **kwargs):
        context = super(Register, self).get_context_data(*args, **kwargs)
        context['applink'] = applink
        context['forumlink'] = forumlink
        context['userform'] = self.get_form(UserCreationForm, 'user')
        context['userprofileform'] = self.get_form(RegistrationForm, 'userprofile')
        return context

    def post(self, request, *args, **kwargs):
        forms = dict((
            ('userform', self.get_form(UserCreationForm, 'user')),
            ('userprofileform', self.get_form(RegistrationForm, 'userprofile')),
        ))
        if all([f.is_valid() for f in forms.values()]):
            return self.form_valid(forms)
        else:
            return self.form_invalid(forms)

    def get_form(self, form_class, prefix):
        return form_class(**self.get_form_kwargs(prefix))

    def get_form_kwargs(self, prefix):
        kwargs = super(Register, self).get_form_kwargs()
        kwargs.update({'prefix': prefix})
        return kwargs

    def form_valid(self, forms):
        user = forms['userform'].save()
        userprofile = forms['userprofileform'].save(commit=False)
        userprofile.user_id = user.id
        userprofile.save()
        return HttpResponseRedirect(self.get_success_url())

    def get(self, request, *args, **kwargs):
        return self.render_to_response(self.get_context_data())