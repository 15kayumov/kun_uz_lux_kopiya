from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(blank=True)
    text = models.TextField( )
    title2=models.CharField(max_length=200)
    text2 = models.TextField()


    def str(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail',args=[str(self.pk)])
class Mir(models.Model):
    title = models.CharField(max_length=200)
    img = models.ImageField(blank=True)
    text = models.TextField( )
    title2=models.CharField(max_length=200)
    text2 = models.TextField()


    def str(self):
        return self.titl
    
    def get_absolute_url(self):
        return reverse('mir_detail',args=[str(self.pk)])
