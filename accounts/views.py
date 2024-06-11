from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
import re
from accounts.forms import UserForm
from django.contrib.auth.forms import UserCreationForm
def login_view(request):
    error = None
    if request.method == 'POST':
        username_or_email = request.POST.get("username")
        password = request.POST.get("password")
        user = None
        
        # Check if the input is an email address
        if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', username_or_email):
            try:
                user = User.objects.get(email=username_or_email)
                username = user.username
            except User.DoesNotExist:
                error = "User with this email does not exist"
        else:
            username = username_or_email

        if not error:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                error = 'Invalid credentials'

    form = AuthenticationForm()
    context = {'form': form, 'error': error}
    return render(request, 'accounts/login.html', context)
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            email = data['email']
            password = data['password']
            confirm_password = request.POST.get('confirm')
            if not User.objects.filter(email=email).exists() and password == confirm_password:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                return redirect('/accounts/login')
            else:
                error_message = 'User already exists or passwords do not match'
                return render(request, 'accounts/signup.html', {'form': form, 'error': error_message})
        else:
            error_message = 'Invalid form data'
            return render(request, 'accounts/signup.html', {'form': form, 'error': error_message})

    form = UserForm()
    return render(request, 'accounts/signup.html', {'form': form})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')
