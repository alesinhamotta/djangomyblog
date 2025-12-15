# djangomyblog/blog/forms.py

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    # O meta interior da classe UserCreationForm já define os campos básicos.
    # Nós só precisamos dizer ao nosso formulário para incluir o 'email'.
    class Meta(UserCreationForm.Meta):
        # Campos que queremos no formulário
        fields = UserCreationForm.Meta.fields + ('email',) 
        # O UserCreationForm.Meta.fields é ('username',)
        # Então, fields será ('username', 'email')