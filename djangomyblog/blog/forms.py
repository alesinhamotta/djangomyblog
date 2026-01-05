# djangomyblog/blog/forms.py

from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Comment


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Escreva seu comentário aqui...'})
        }
