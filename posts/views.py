from django.shortcuts import redirect, render
from .models import Post
from .forms import PostForm
# Create your views here.

def post_list(request):
    data = Post.objects.all()
    context ={"post_list":data}
    return render(request ,'posts/post_list.html',context)

#what is type of request
# are requext is parameter i can change it or no ?

def post_detail(request ,pk):
    post_data =Post.objects.get(id =pk)

    context = {'post_detail' :post_data}
    return render(request ,'posts/post_detail.html' ,context)


def creat_post(request):
    if request.method =='POST':
        form =PostForm(request.POST ,request.FILES) 
        if form.is_valid():
            myform =form.save(commit=False)
            myform.author =request.user
            myform.save()
            return redirect('/posts/')

    else:
        form =PostForm()
    return render(request ,'posts/creat_post.html' ,{'form':form})




from django.views.generic import ListView ,DetailView
class PostList(ListView):
    model =  Post
    # context_object_name ='posts'

class PostDetail(DetailView):
    model =Post
