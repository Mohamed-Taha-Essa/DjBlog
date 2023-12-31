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
from posts.views import (post_list ,post_detail ,creat_post,
                         edit_post,delete_post,comment_edit,
                         comment_delete)
from posts.views2 import PostList ,PostDetail,CreatePost,UpdatePost,DeletePost

from posts.api import ListApiView,DetailApiView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

...

schema_view = get_schema_view(
   openapi.Info(
      title="Blog API",
      default_version='v1',
      description="Full Blog API",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('add_post/', creat_post, name='add_post'),
    path('edit_post/<int:pk>/', edit_post, name='edit_post'),
    path('delete_post/<int:pk>/', delete_post, name='delete_post'),

    path('posts/',post_list ,name='post-list' ),
    path('posts/<int:pk>',post_detail,name='post-detail'),
   
# operation on comment
    path('posts/<int:post_pk>/<int:comment_pk>/',comment_edit ,name='comment-edit'),
    path('posts/<int:post_pk>/<int:comment_pk>/delete/',comment_delete ,name='comment-delete'),

# API
    path('api-auth/', include('rest_framework.urls')),
    path('posts/api/' ,ListApiView.as_view()),
    path('posts/api/<int:pk>' ,DetailApiView.as_view()),


### drf-yasg
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
 


#class basec view.
    # path('posts/',PostList.as_view()),
    # path("posts/add", CreatePost.as_view()),
    # path('posts/<int:pk>',PostDetail.as_view()),
    # path('posts/<int:pk>/update',UpdatePost.as_view()),
    # path('posts/<int:pk>/delete',DeletePost.as_view()),

  
]

urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
