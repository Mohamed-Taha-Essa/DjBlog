#view
from rest_framework.decorators import api_view

from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response

'''
@api_view(['GET'])
def post_list_api(request):
    post = Post.objects.all()
    data =PostSerializer(instance=post,many =True).data
    return Response({'data':data})


@api_view(['GET' ,'DELETE','PUT'])
def post_detail_api(request,pk):
    post =Post.objects.get(id=pk)
    data =PostSerializer(post).data
    return Response({'data':data})'''


from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class ListApiView(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class =PostSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['author', 'draft']
    search_fields = ['title', 'content']
    ordering_fields =['public_date_time']


class DetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class =PostSerializer