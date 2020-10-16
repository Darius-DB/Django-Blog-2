from django import forms
from .models import Comments


class CommentForm(forms.Form):
    class Meta:
        model = Comments
        fields = ['content']