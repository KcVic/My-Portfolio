from django.contrib import admin
from .models import about, Skill
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(about)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

# admin.site.register(about, AboutAdmin)
@admin.register(Skill)
class SkillAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)    

# admin.site.register(Skill, AboutAdmin)
