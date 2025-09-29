from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    """
    Formulario para el registro de nuevos usuarios.
    
    Hereda de `UserCreationForm` de Django y añade el campo 'email'
    al formulario de registro estándar.
    """
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',)