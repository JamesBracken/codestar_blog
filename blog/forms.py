from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    Creates a form for :model:`blog.Comment`
    """
    class Meta:
        model = Comment
        fields = ('body',)