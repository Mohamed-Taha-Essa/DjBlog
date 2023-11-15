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
    return render(request ,'posts/edit_post.html' ,{'form':form})


def delete_post(request,pk):
    post =Post.objects.get(id =pk)
    post.delete()
    return redirect('/posts/')


from django.views.generic import ListView ,DetailView,CreateView,DeleteView,UpdateView
class PostList(ListView):            #obj_name =name of model_list--->post_list or objects
    model =  Post                    #template name =post_list.html          
    # context_object_name ='posts'

class PostDetail(DetailView):           #post 
    model =Post                          #post_detail.html

class CreatePost(CreateView):
    model =Post
    fields ='__all__'
    success_url ='/posts/'

class UpdatePost(UpdateView):
    model = Post
    template_name = 'posts/update.html'

    fields ='__all__'   
    success_url = ('/posts/')  # URL to redirect after successful form submission    

class DeletePost(DeleteView):
    model = Post
    success_url =('/posts/')  # URL to redirect after successful deletion