"""
Definition of views.
"""

from datetime import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['title'] = 'Home Page'
        context['sidebar']=  'Home'
        context['year'] = datetime.now().year
        return context

    # def get(self,request, *args, **kwargs):
    #     if request.user.is_authenticated:
    #         return HttpResponseRedirect(reverse('about'))
    #     return super().get(request, *args, **kwargs)


class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['title'] = 'Contact'
        context['sidebar'] = 'Contact'
        context['message'] = 'Your contact page.'
        context['year'] = datetime.now().year
        return context

class AboutView(TemplateView):
    template_name = 'about.html'
    extra_context={
         'title': 'About',
         'sidebar': 'About',
         'year': datetime.now().year,
    }

class LoginsuccessView(TemplateView):
    template_name = 'loginsuccess.html'
    extra_context={
         'year': datetime.now().year,
    }

class ThanksView(TemplateView):
    template_name = 'thanks.html'
    extra_context={
         'year': datetime.now().year,
    }
