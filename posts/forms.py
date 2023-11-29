<<<<<<< HEAD
# posts/forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields ='__all__'
=======
from django import forms
from .models import Post ,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model =Post
        #fields ='__all__'
        exclude =('author',)

class CommentForm(forms.ModelForm):
    class Meta:
        model =Comment
        fields =['comment' ,'user']
>>>>>>> 42a0e17658b98c4b6411c16a4b015939e8acfdec
