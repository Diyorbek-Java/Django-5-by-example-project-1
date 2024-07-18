from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
    name=forms.CharField(max_length=255)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

class CommentForm:
    class Meta:
        model = Comment
        fields = ['name','email','body']