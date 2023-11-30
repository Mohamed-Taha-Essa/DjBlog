#view
from rest_framework.decorators import api_view

from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import generics


@api_view(['GET'])
def post_list_api(request):
    post = Post.objects.all()
    data =PostSerializer(instance=post,many =True).data
    return Response({'data':data})


@api_view(['GET' ,'DELETE','PUT'])
def post_detail_api(request,pk):
    post =Post.objects.get(id=pk)
    data =PostSerializer(post).data
    return Response({'data':data})


class ListApiView(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class =PostSerializer

class DetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class =PostSerializer