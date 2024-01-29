# -*- coding: utf8 -*-
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from photo_competition.forms import LoginUserForm, RegisterUserForm


def logout_user(request):
    """Log out"""
    logout(request)
    return redirect('index')


class UserRegisterView(CreateView):
    # Какая форма исп-ся для реги-ции
    form_class = RegisterUserForm

    # Шаблон котор будет исполь-ся
    template_name = 'register.html'

    # Когда пользователь ввел свои данные
    def form_valid(self, form):
        # Сохраняю пользователя
        user = form.save()

        # Логиню пользователя
        login(self.request, user)
        return redirect('index')


class UserLoginView(LoginView):
    # Форма для логина
    form_class = LoginUserForm
    template_name = 'login.html'

    # В случае успеха
    def get_success_url(self):
        return reverse_lazy('index')
