"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static
from posts.views import post_list ,post_detail ,creat_post,edit_post,delete_post,comment_edit
from posts.views2 import PostList ,PostDetail,CreatePost,UpdatePost,DeletePost

from posts.api import post_list_api


urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('add_post/', creat_post, name='add_post'),
    path('edit_post/<int:post_id>/', edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', delete_post, name='delete_post'),

    path('posts/',post_list ,name='post-list' ),
    path('posts/<int:pk>',post_detail,name='post-detail'),
    path("posts/new", creat_post),
    path("posts/<int:pk>/edit", edit_post),
    path('posts/<int:pk>/delete',delete_post),

# operation on comment
    path('posts/<int:post_pk>/<int:comment_pk>/',comment_edit ,name='comment-edit'),

# API
    path('posts/api/' ,post_list_api)





#class basec view.
    # path('posts/',PostList.as_view()),
    # path("posts/add", CreatePost.as_view()),
    # path('posts/<int:pk>',PostDetail.as_view()),
    # path('posts/<int:pk>/update',UpdatePost.as_view()),
    # path('posts/<int:pk>/delete',DeletePost.as_view()),

  
]

urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
