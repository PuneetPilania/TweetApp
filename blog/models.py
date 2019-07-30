from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse


class Post(models.Model):
    title=models.CharField(max_length=100,null=True,blank=True)
    content=models.TextField(null=True,blank=True)
    date_posted=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='blog/image',default="",null=True,blank=True)
    video=models.FileField(upload_to='blog/video',default="",null=True,blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
    	return reverse('blog-detail' ,kwargs={'pk': self.pk})

  




