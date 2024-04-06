from django import forms
from blog.models import Post, Comment
#from captcha.fields import CaptchaField

class CommentForm(forms.ModelForm):
    #captcha = CaptchaField()
    class Meta:
        model = Comment
        
        fields = ['post', 'name', 'email', 'subject', 'message']
