from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

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


class Messege(models.Model):
    messege_from=models.TextField(blank=False,null=False,default=None)
    messege_to=models.TextField(blank=False,null=False,default=None)
    messege=models.TextField(blank=False,null=False)
    date_time=models.DateTimeField(default=timezone.now)


    def get_absolute_url(self):
        return reverse('messege', kwargs={'user': self.messege_to})

    def __str__(self):
        return self.messege_to

    



  




