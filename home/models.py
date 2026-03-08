from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class about(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    profile_pic = CloudinaryField('image', null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    CATEGORY_CHOICES = (
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('tools', 'Tools'),
    )
    name = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"