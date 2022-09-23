from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from .models import Contact
# Create your views here.

class ContactViews(CreateView):
    model = Contact
    fields = ('__all__')
    template_name = 'contact.html'

class ResumeViews(TemplateView):
    template_name = 'resume.html'

class AboutViews(TemplateView):
    template_name = 'about.html'

class WorkViews(TemplateView):
    template_name = 'work.html'

class ProfileView(TemplateView):
    template_name = "profile.html"