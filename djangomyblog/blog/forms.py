from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Comment


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=False)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["comment"]
        widgets = {
            "comment": forms.Textarea(
                attrs={
                    "rows": 4,
                    "placeholder": "Escreva seu comentário"
                }
            )
        }

    def clean_comment(self):
        comment = self.cleaned_data["comment"].strip()
        if not comment:
            raise forms.ValidationError("O comentário não pode estar vazio.")
        return comment
