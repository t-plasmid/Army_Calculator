"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['title'] = 'Home Page'
        context['year'] = datetime.now().year
        return context

class ContactView(TemplateView):
    template_name = 'app/contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['title'] = 'Contact'
        context['message'] = 'Your contact page.'
        context['year'] = datetime.now().year
        return context

class AboutView(TemplateView):
    template_name = 'app/about.html'
    extra_context={
         'title': 'About',
         'message': 'Your application description page.',
         'year': datetime.now().year,
    }
