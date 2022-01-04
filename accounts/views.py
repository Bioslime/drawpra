from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, TemplateView
from .forms import LoginForm, UserCreateForm
from django.contrib import messages
from django.urls import reverse, reverse_lazy


class UserRegister(CreateView):
    template_name = "accounts/register.html"
    form_class = UserCreateForm
    success_url = reverse_lazy("accounts:top")

    def form_valid(self, form):
        messages.success(self.request, "新規データを作成しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, "作成に失敗しました")
        return super().form_invalid(form)


class Login(LoginView):
    form_class = LoginForm
    template_name = 'accounts/login.html'


class Logout(LogoutView):
    # template_name = 'menu/top.html'
    pass


# class UserCreateDone(generic.CreateView):
#     pass
