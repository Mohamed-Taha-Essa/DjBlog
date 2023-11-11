from django.shortcuts import render
from .models import Post
# Create your views here.

def list_posts(request):
    data = Post.objects.all()
    


    return render(request ,'posts/list_post.html',{"taha":data})