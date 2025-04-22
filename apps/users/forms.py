from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
#
# class CustomUserCreationForm(UserCreationForm):
#     email = forms.EmailField(required=True, label="Email")
#
#     class Meta:
#         model = CustomUserManager
#         fields = ('email', 'username', 'password1', 'password2')
#
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if CustomUserManager.objects.filter(email=email).exists():
#             raise forms.ValidationError("Этот email уже зарегистрирован.")
#         return email
class LoginForm(AuthenticationForm):
    """
    Аутенти
    """
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Имя пользователя'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Пароль'}))

class RegistrationForm(UserCreationForm):
    """
    Регис
    """
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Пароль'})),
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Подтвердите пароль'}))

    class Meta:
        model = User
        fields = ['username', 'email']
        widget = {'username': forms.Textarea(attrs={'class': 'form-control',
                                                             'placeholder': 'Имя пользователя'}),
                'email' : forms.EmailInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Почта'})}