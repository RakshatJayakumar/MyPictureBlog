from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.urls import reverse
from django.shortcuts import render, redirect

class UserLoginView(LoginView):
    template_name = "authapp/login.html"
    redirect_authenticated_user = True

    def get_success_url(self):
        return "/blog/post"


class RegisterPage(FormView):
    template_name = "authapp/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)

        return super(RegisterPage, self).form_valid(form)

    def get_success_url(self):
        return reverse("post_list")

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.get_success_url())
        return super(RegisterPage, self).get(*args, **kwargs)