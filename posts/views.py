from django.shortcuts import redirect, render
from .models import Post ,Comment
from .forms import PostForm
from .forms import CommentForm

# Create your views here.

def post_list(request):
    data = Post.objects.all()
    context ={"post_list":data}
    return render(request ,'posts/post_list.html',context)

#what is type of request
# are requext is parameter i can change it or no ?

def post_detail(request ,pk):
    post_data =Post.objects.get(id =pk)
    comments = Comment.objects.filter(post =post_data)
     
    if request.method =='POST' :
        form =CommentForm(request.POST)
        if form.is_valid():
            myform =  form.save(commit=False)
            myform.post =post_data
            myform.save()
    else:
        form =CommentForm()



    context = {'post' :post_data,
               'comments':comments,
                'form':form,
               }
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
    return render(request ,'posts/post_form.html' ,{'form':form})

def edit_post(request ,pk):
    post =Post.objects.get(id =pk)

    if request.method =='POST':
        form =PostForm(request.POST ,request.FILES ,instance=post) 
        if form.is_valid():
            myform =form.save(commit=False)
            myform.author =request.user
            myform.save()
            return redirect('/posts/')

    else:
        form =PostForm(instance=post)
    return render(request ,'posts/update.html' ,{'form':form})


def delete_post(request,pk):
    post =Post.objects.get(id =pk)
    post.delete()
    return redirect('/posts/')


