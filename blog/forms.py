from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, label='你的名字')
    email = forms.EmailField(label='你的邮箱')
    to = forms.EmailField(label='要分享的好友邮箱')
    comments = forms.CharField(required=False, widget=forms.Textarea, label='快把你对该文章的看法告诉好友')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class SearchForm(forms.Form):
    query = forms.CharField(label='输入关键字')
