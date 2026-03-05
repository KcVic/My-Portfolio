from django.shortcuts import render
from django.views.generic import TemplateView
from .models import about, Skill

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home/home.html'

class AboutView(TemplateView):
    template_name = 'home/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = about.objects.all()
        context['skill'] = Skill.objects.all()
        return context
