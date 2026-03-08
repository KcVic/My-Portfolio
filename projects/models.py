from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class project(models.Model):
    CATEGORY_CHOICES = (
        ('webapps', 'Web Applications'),
        ('maps', 'Maps'),
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    featured_image = CloudinaryField('image', default='placeholder.jpg')
    title = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    pdf = models.FileField(upload_to='projects/', blank=True, null=True)
    technology = models.CharField(max_length=100)

    def __str__(self):
        return self.title

