from django.db import models
from django.contrib.auth.context_processors import auth
from django.contrib.auth.models import User
# Create your models here.
class BBS(models.Model):
    title=models.CharField(max_length=25)
    category=models.ForeignKey('Category')
    summary=models.CharField(max_length=60,blank=True)
    content=models.TextField()
    author=models.ForeignKey('BBS_user')
    view_count=models.IntegerField()
    ranking=models.IntegerField()
    create_date=models.DateField(auto_now_add=True)
    update_date=models.DateField(auto_now_add=True)
    def __unicode__(self):
        return self.title

class Category(models.Model):
    name=models.CharField(max_length=30,unique=True)
    administrator=models.ForeignKey('BBS_user')
    def __unicode__(self):
        return self.name
    
class BBS_user(models.Model):
    user=models.OneToOneField(User)
    signature=models.CharField(max_length=128,default='this guy is too lazy to leave anything here!')
    headimg=models.ImageField(upload_to='image/',default='image/author.jpg')
    def __unicode__(self):
        return self.user.username
