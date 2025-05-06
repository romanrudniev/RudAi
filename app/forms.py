from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


class PromptForm(forms.Form):
    MODEL_CHOICES = [
        ("gpt-3.5-turbo", "GPT-3.5 Turbo"),
        ("gpt-4.1", "GPT-4"),
        ("dall-e-3", "DALL-E 3"),
        ("gpt-image-1", "GPT-Image-1"),
    ]

    prompt = forms.CharField(label="Введіть запит:", max_length=1000, widget=forms.Textarea)
    model_type = forms.ChoiceField(label="Оберіть модель", choices=MODEL_CHOICES, initial="gpt-3.5-turbo")



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
