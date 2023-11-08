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
5-category
6-comment

'''
# Create your models here.

class Posts(models.Model):
    author =models.ForeignKey(User, related_name='post_author'  ,  on_delete=models.CASCADE)
    title = models.CharField( max_length=50)
    content=models.TextField(max_length=2000)
    draft =models.BooleanField(default=True)

    public_date_time = models.DateTimeField()
    image = models.ImageField(upload_to='post')
    tags = TaggableManager()

    def __str__(self):
        return self.title
    

