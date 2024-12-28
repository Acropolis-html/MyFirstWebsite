from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.forms import TextInput, PasswordInput,EmailInput
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget = TextInput(attrs={'class': 'form-input login'}))
    email = forms.EmailField(widget = EmailInput(attrs={'class': 'form-input email'}))
    password1 = forms.CharField(label='Пароль', widget = PasswordInput(attrs={'class': 'form-input password1'}))
    password2 = forms.CharField(label='Повтор пароля', widget = PasswordInput(attrs={'class': 'form-input password2'}))
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=TextInput(attrs={'class': 'form-input login'}))
    password = forms.CharField(label='Пароль', widget=PasswordInput(attrs={'class': 'form-input password'}))

from django import forms
from django.contrib.auth.models import User


class EditProfileForm(forms.ModelForm):
    current_password = forms.CharField(
        label='Текущий пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите текущий пароль'}),
        required=True
    )
    new_password = forms.CharField(
        label='Новый пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите новый пароль'}),
        required=True
    )
    confirm_password = forms.CharField(
        label='Подтверждение пароля',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Подтвердите новый пароль'}),
        required=True
    )

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя пользователя'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Введите email'}),
        }
        labels = {
            'username': 'Имя пользователя',
            'email': 'Электронная почта',
        }

    def clean(self):
        cleaned_data = super().clean()

        current_password = cleaned_data.get('current_password')
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')

        if new_password and confirm_password:
            if new_password != confirm_password:
                raise ValidationError("Новый пароль и подтверждение пароля не совпадают.")

        if current_password:
            user = self.instance
            if not user.check_password(current_password):
                raise ValidationError("Текущий пароль неверен.")

        return cleaned_data