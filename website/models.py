from django.db import models
from django.urls import reverse


# Create your models here.

class Institution(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255,  null=True)

    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_date']
        
    def __str__(self):
        return self.name


class Certificates(models.Model):   
    image = models.ImageField(upload_to = 'blog/', default='blog/default.jpg')
    title = models.CharField(max_length=255)
    institution = models.ForeignKey(Institution, on_delete=models.SET_NULL, null=True)
    issu_date = models.DateTimeField(null=True)
    field_name = models.URLField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-issu_date']
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("website:single", kwargs={'pid': self.id})
    
class NewsLetter(models.Model):
    email = models.EmailField()
    
    def __str__(self):
        return self.email