from django.shortcuts import get_object_or_404, render ,redirect
from .models import Post
from .forms import PostForm

# Create your views here.

def post_list(request):
    data = Post.objects.all()
    context ={"taha":data}
    return render(request ,'posts/post_list.html',context)

#what is type of request
# are requext is parameter i can change it or no ?

def post_detail(request ,pk):
    post_data =Post.objects.get(id =pk)

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