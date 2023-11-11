from django.shortcuts import render
from .models import Post
# Create your views here.

def list_posts(request):
    data = Post.objects.all()
    context ={"taha":data}
    return render(request ,'posts/list_post.html',context)

#what is type of request
# are requext is parameter i can change it or no ?

def post_detail(request ,pk):
    post_data =Post.objects.get(id =pk)

    context = {'post_detail' :post_data}
    return render(request ,'posts/post_detail.html' ,context)