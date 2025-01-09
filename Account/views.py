from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.

def login_request(request):
    
    if request.user.is_authenticated:
        return redirect('product:home')
    
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('product:home')
        else:
            return render(request, 'Account/login.html', {'error': 'Invalid username or password'})
        
    return render(request, 'Account/login.html')


def register_request(request):
    
    if request.user.is_authenticated:
        return redirect('product:home')
    
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        
        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, 'Account/register.html', {
                    'error': 'Username already exists',
                    'firstname': firstname,
                    'lastname': lastname,
                    'username': username,
                    'email': email
                    })
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, 'Account/register.html', {
                        'error': 'Email already exists',
                        'firstname': firstname,
                        'lastname': lastname,
                        'username': username,
                        'email': email
                        })
                else:
                    user = User.objects.create_user(username=username, email=email, password=password, first_name=firstname, last_name=lastname)
                    user.save()
                    return redirect('account:login')
        else:
            return render(request, 'Account/register.html', {
                'error': 'Passwords do not match',
                'firstname': firstname,
                'lastname': lastname,
                'username': username,
                'email': email
                })
    return render(request, 'Account/register.html')

def logout_request(request):
    logout(request)
    return redirect('product:home')