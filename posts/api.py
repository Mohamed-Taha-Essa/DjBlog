#view
from rest_framework.decorators import api_view

from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response

@api_view(['GET'])

def post_list_api(request):
    post = Post.objects.all()
    data =PostSerializer(instance=post,many =True).data
    return Response({'data':data})
