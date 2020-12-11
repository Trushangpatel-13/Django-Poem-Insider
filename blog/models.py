from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse,reverse_lazy
from ckeditor.fields import RichTextField
from datetime import datetime,time
# Create your models here.
class CategoryList(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
    def get_absolute_url (self):
        return reverse('article-detail',args=(str(self.id)))


class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True,blank=True,upload_to="images/profile/")
    social_media_insta = models.CharField(null=True,blank=True,max_length=100)
    social_media_github = models.CharField(null=True, blank=True, max_length=100)
    social_media_pinterest = models.CharField(null=True, blank=True, max_length=100)

    def __str__(self):
        return str(self.user)
    def get_absolute_url (self):
        return reverse('home')



class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True,blank=True,upload_to="images/")
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    body = RichTextField(blank=True,null=True)
    #body = models.TextField()
    pub_Date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=25,default='coding')
    likes = models.ManyToManyField(User,related_name='blog_posts')
    snippet = models.CharField(max_length=100)
    def __str__(self):
        return str(self.title)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    def get_absolute_url (self):
        return reverse('article-detail',args=(str(self.id)))
        #return reverse('home')

class Comment(models.Model):
    post = models.ForeignKey(Post,related_name = "comments",on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title,self.name)
