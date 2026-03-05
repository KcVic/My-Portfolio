from django.views.generic import TemplateView
from .models import project

# Create your views here.
class ProjectsView(TemplateView):
    template_name = 'projects/projects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = project.objects.all()
        return context
