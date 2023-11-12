from django.utils import timezone
from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User

'''
posts:
1-title
2-content
3-draft
4-public-date
4-img
-tags  --- using library tagit from django packages


5-category
6-comment

'''
# Create your models here.

class Post(models.Model):
    author =models.ForeignKey(User, related_name='post_author'  ,  on_delete=models.CASCADE)
    title = models.CharField( max_length=50)
    content=models.TextField(max_length=20000)
    draft =models.BooleanField(default=True)

    public_date_time = models.DateTimeField( auto_now=True)
    image = models.ImageField(upload_to='post')
    tags = TaggableManager()

    category = models.ForeignKey("Category", related_name="post_category", on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.title
    

class Category(models.Model):
    name =models.CharField(max_length=50)
    #relation ship between category and post  one to many or many to many 
    # one category have mulible post.
    # one post habe one category or more .

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    #relation ship between comment and post  one to many 
    # one post have mulible comment.
    #when add comment determine the post
    post = models.ForeignKey(Post, related_name='comment_posts', on_delete=models.SET_NULL ,null=True)

    user = models.CharField( max_length=50)
    comment= models.TextField(max_length=100)
    created_at = models.DateTimeField( default= timezone.now )
    
    def __str__(self):
        return self.user
    