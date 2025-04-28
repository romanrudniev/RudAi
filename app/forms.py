from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class PromptForm(forms.Form):
    prompt = forms.CharField(label="Enter your prompt", max_length=1000, widget=forms.Textarea)


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Паролі не співпадають!")


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Ім'я користувача")
    password = forms.CharField(label="Пароль", widget=forms.PasswordInput)
