from django.views.generic import TemplateView
from django.conf import settings
from django.http import FileResponse, HttpResponseNotFound
from .models import project

# Create your views here.
class ProjectsView(TemplateView):
    template_name = 'projects/projects.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['projects'] = project.objects.all()
        return context

def download_pdf(request, pk):
    try:
        proj = project.objects.get(pk=pk)
        if proj.pdf:
            return FileResponse(open(proj.pdf.path, 'rb'), as_attachment=True, filename=proj.pdf.name)
        return HttpResponseNotFound("Pdf not found")
    except project.DoesNotExist:
        return HttpResponseNotFound("Project not found")
