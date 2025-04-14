from django import forms
from .models import CollaborateRequest 


class CollaborateForm(forms.ModelForm):
    """
    Creates a form for :model:`about.CollaborateRequest`
    """
    class Meta:
        model = CollaborateRequest
        fields = ("name", "email", "message", )