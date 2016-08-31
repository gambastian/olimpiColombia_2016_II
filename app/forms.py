from django import forms
from django.core.validators import validate_email

from .models import Usuario

class UsuarioRegistroForm(forms.ModelForm):

    password2 = forms.CharField(widget=forms.PasswordInput(), label ='Ingrese nuevamente el password')
    class Meta:
        model = Usuario
        widgets = {
            'password' : forms.PasswordInput(),
        }

        fields = ['nombre','apellido','email','username','password','password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if Usuario.objects.filter(email=email):
            raise forms.ValidationError('Ya existe un usuario con el email registrado')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if Usuario.objects.filter(username=username):
            raise forms.ValidationError('Ya existe un usuario con el username registrado')
        return username

    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError('las claves no coinciden')
        return password2