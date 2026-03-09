from django.contrib import admin
from .models import project
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
# admin.site.register(project)
@admin.register(project)
class ProjectAdmin(SummernoteModelAdmin):
    summernote_fields = ('description',)
