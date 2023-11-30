#form 
from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields=['id','username','email']



class PostSerializer(serializers.ModelSerializer):
    author =UserSerializer()
    category =serializers.StringRelatedField()
    class Meta:
        model = Post
        fields= '__all__'

# class PostForm(forms.ModelForm):
#     class Meta:
#         model =Post
#         #fields ='__all__'
#         exclude =('author',)