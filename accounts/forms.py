from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from .models import CustomUser


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


class UserCreateForm(UserCreationForm):
    username = forms.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ("username", "password1", "password2", "email",)

