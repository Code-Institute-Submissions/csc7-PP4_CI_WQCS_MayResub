# Code copied from Code Institute "I Think Therefore I Blog" project
# on December 23rd, 2022 at 15:17

from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        