from datetime import datetime
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms
from django.http import HttpResponseRedirect


# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy("login")
    template_name = "accounts/signup.html"
    extra_context = {
        'title': 'Sign up',
        'sidebar': 'Account',
        'year': datetime.now().year,
    }

class ContactView(CreateView):
    template_name = 'accounts/contact.html'
    form_class = forms.ContactForm
    success_url = reverse_lazy("accounts:contact")

