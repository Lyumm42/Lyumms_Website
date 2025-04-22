from pyexpat.errors import messages

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from .forms import LoginForm, RegistrationForm
from .models import User

def register_view(request):
    if request.method == 'POST':
        form = User(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = User()
    return render(request, 'users/register.html', {'form': form})

def login_registration(request):
    context = {'title': "Войти или эарег",
               'login_form': LoginForm,
               'registration_form': RegistrationForm}
    return  render(request, 'users/register.html', context)



def user_login(request):
    form = LoginForm(data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('index')
    else:
        messages.error(request, 'Не вкерное имя польз или пароль')
        return redirect('login_registration')


def user_logout(request):
    logout(request)
    return redirect('index')


def registrations(request):
    form = RegistrationForm(data=request.POST)
    if form.is_valid():
        form.save()
        messages.success(request, 'Аккаунт пользователя успешно создан')
    else:
        for error in form.errors:
            messages.error(request, form.errors[error].as_text())
        messages.error(request, 'Не вкерное имя польз или пароль')
    return  redirect('login_registration')



