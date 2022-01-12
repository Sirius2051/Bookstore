# from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from django.views.generic import CreateView, TemplateView

from .models import Account

from .forms import SignUpForm
from django.contrib.auth.views import LoginView, LogoutView

from Books.models import Book

class SignInView(LoginView):
    template_name = 'accounts/login.html'

class SignUp(CreateView):
    model = Account
    form_class = SignUpForm
    template_name = 'accounts/signup.html'

    def formValid(self, form):
        form.save()
        user = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=user, password=password)
        login(self.request, user)

        return redirect('/')

class Welcome(TemplateView):
    template_name = 'accounts/welcome.html'

    context_object_name = 'books_list'    
    def get_queryset(self):
        return Book.objects.all()

class SignOutView(LogoutView):
    pass