<<<<<<< HEAD
from django.shortcuts import get_object_or_404, render ,redirect
from .models import Post
from .forms import PostForm
=======
from django.shortcuts import redirect, render
from .models import Post ,Comment
from .forms import PostForm
from .forms import CommentForm
>>>>>>> 42a0e17658b98c4b6411c16a4b015939e8acfdec

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
            return redirect(f'/posts/{pk}')
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

def comment_edit(request,post_pk ,comment_pk):
    post =Post.objects.get(id =post_pk)
    comment = Comment.objects.get(id=comment_pk)
    if request.method =='POST':
        form =CommentForm(request.POST,instance=comment)
        if form.is_valid():
            myform =form.save(commit=False)
            myform.post =post
            myform.save()
            return redirect(f'/posts/{post_pk}')

            ''' if 'action' in request.POST:
                    if request.POST['action'] == 'Update':
                        if form.is_valid():
                            myform =form.save(commit=False)
                            myform.post =post
                            myform.save()
                            return redirect(f'/posts/{post_pk}')
                    elif request.POST['action'] == 'Cancel':
                        return redirect(f'/posts/{post_pk}')
            '''

    else:
        form =CommentForm(instance=comment)

    context = {'comments':comment,
               'form':form ,
               'post':post ,}
    return render(request ,'posts/comment_edit.html' ,context)


<<<<<<< HEAD
    context = {'post_detail' :post_data}
    return render(request ,'posts/post_detail.html' ,context)

def add_post(request):
    if request.method =='POST':
        form =PostForm(request.POST ,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')

    else:
        form = PostForm()

    return render(request, 'posts/add_post.html', {'form': form})


def edit_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Redirect to the blog post list view
    else:
        form = PostForm(instance=post)

    return render(request, 'posts/edit_post.html', {'form': form, 'post': post})


def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    return redirect('post_list') 
from django.views.generic import ListView ,DetailView

class PostList(ListView):
    model = Post

class PostDetail(DetailView):
    model =Post
=======
>>>>>>> 42a0e17658b98c4b6411c16a4b015939e8acfdec
