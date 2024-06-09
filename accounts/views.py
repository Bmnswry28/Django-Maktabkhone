from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
import re
from accounts.forms import UserForm

def login_views(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Check if the input is an email address
            if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', username):
                try:
                    user = User.objects.get(email=username)
                    username = user.username
                except User.DoesNotExist:
                    form.add_error(None, "Invalid email or password")
                    return render(request, 'accounts/login.html', {'form': form})

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form.add_error(None, "Invalid username or password")
        else:
            print("Form errors: ", form.errors)  # Debugging information
            print("Cleaned data: ", form.cleaned_data)  # Debugging information
    else:
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form': form})

def singup_views(request):
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

            if User.objects.filter(email=email).exists():
                form.add_error('email', "Email already exists")
            elif password != confirm_password:
                form.add_error('password', "Passwords do not match")
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                return redirect('/accounts/login')
    else:
        form = UserForm()
    
    return render(request, 'accounts/signup.html', {'form': form})

def loguot_views(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')
