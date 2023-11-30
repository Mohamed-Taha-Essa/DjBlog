#form 
from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author =serializers.StringRelatedField()
    category =serializers.StringRelatedField()
    class Meta:
        model = Post
        fields= '__all__'

# class PostForm(forms.ModelForm):
#     class Meta:
#         model =Post
#         #fields ='__all__'
#         exclude =('author',)