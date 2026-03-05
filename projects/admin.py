from django.contrib import admin
from .models import project
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(project)
class ProjectAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)

# admin.site.register(project, ProjectAdmin)
