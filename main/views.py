from lib2to3.fixes.fix_input import context
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth.views import LoginView
from django.template.context_processors import request
from django.contrib.auth import login, logout, update_session_auth_hash
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView

from .forms import RegisterUserForm, LoginUserForm, EditProfileForm
from .utils import DataMixin
def index(request):
    return HttpResponse('<h4>фара, сколько ты заплатишь мне за это?<h4>')
# В любом методе мы должны писать request
# <h4> это что-то на HTML короче типа print
# закрыть сервер ctrl + c

def about(request):
    return render(request, 'main/about.html')

def buttons(request):
    return render(request, 'main/buttons.html')

def html(request):
    return render(request,'main/index.html')

def test(request):
    return render(request, 'main/test.html')

# def logout(request):
#     return render(request, 'main/test.html')

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = '/login'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return {**context, **c_def}

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('html')

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Логин')
        return {**context, **c_def}

    def get_success_url(self):
        return reverse_lazy('html')

def LogoutUser(request):
    logout(request)
    return redirect('login')

@login_required
def profile(request):
    return render(request, 'main/profile.html', {'main': request.user})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

            current_password = form.cleaned_data.get('current_password')
            new_password = form.cleaned_data.get('new_password')

            if new_password:
                user = request.user
                user.set_password(new_password)
                user.save()

                update_session_auth_hash(request, user)

                messages.success(request, 'Пароль успешно изменен.')

            messages.success(request, 'Профиль успешно обновлен.')
            return redirect('profile')

    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'main/edit_profile.html', {'form': form})