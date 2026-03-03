from django.db import models

# Create your models here.
class about(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    profile_pic = models.ImageField(upload_to='images/')
    github = models.CharField(max_length=500)
    linkedin = models.CharField(max_length=500)
    email = models.CharField(max_length=500)

    def __str__(self):
        return self.title

class Skill(models.Model):
    CATEGORY_CHOICES = (
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('tools', 'Tools'),
    )
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.get_category_display()})"