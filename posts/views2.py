from django.views.generic import ListView ,DetailView,CreateView,DeleteView,UpdateView
from .models import Post


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