# Utils
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Routing
from django.http import HttpResponseRedirect
from django.http import Http404

# Forms
from .forms import UserRegistrationForm

# Models
from .models import TestProjectUser


def index_page(request):
    template = 'index.html'
    return render(request, template)


def registration_view(request):
    """
    Форма регистрации
    """
    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST or None)
        if registration_form.is_valid():
            new_user = registration_form.save(commit=False)
            new_user.save()
            return redirect('login_page')
    else:
        registration_form = UserRegistrationForm()

    context = {
        'registration_form': registration_form,
    }
    template = 'users/register_page.html'
    return render(request, template, context)


def login_view(request):
    """
    Форма авторизации
    """
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_profile_page', email=request.POST['email'])
        else:
            return redirect('login_page')
    else:
        template = 'users/login_page.html'
        return render(request, template)


@login_required()
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required()
def user_profile(request, email):
    target_user = TestProjectUser.objects.get(email=email)

    context = {
        'target_user': target_user,
    }
    template = 'users/users_private_profile.html'
    return render(request, template, context)
