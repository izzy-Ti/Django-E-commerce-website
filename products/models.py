from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50) 
    discription = models.TextField()
    slug = models.SlugField()
    date = models.DateField(auto_now_add=True)
    banner = models.ImageField(default='fallback.png', blank=True)
    img2 = models.ImageField(default='fallback.png', blank=True)
    img2 = models.ImageField(default='fallback.png', blank=True)
    price = models.CharField(max_length=50, default='__')


    def __str__(self):
        return self.title