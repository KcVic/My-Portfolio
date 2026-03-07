from django.shortcuts import render
from django.views.generic import TemplateView
from post_office import mail
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

class ContactView(TemplateView):
    template_name = 'home/contact.html'


    def post(self, request, *args, **kwargs):
        name = request.POST.get('name', 'Anonymous')
        email = request.POST.get('email', 'No email')
        subject = request.POST.get('subject', 'Portfolio Contact Form Submission')
        message = request.POST.get('message', '')
        
        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            mail.send(
                'akomavictor@gmail.com',
                subject=subject,
                message=body,
                priority='now',
            )
            return render(request, self.template_name, {'success': True})
        except Exception:
            return render(request, self.template_name, {'error': True})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['success'] = self.request.GET.get('success', False)
        context['error'] = self.request.GET.get('error', False)
        return context