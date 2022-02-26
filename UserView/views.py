from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm
from django.contrib import messages

def home_page(request):
    return render(request, 'home/home.html')

def signup_page(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = SignUpForm()
		if request.method == 'POST':
			form = SignUpForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)
				return redirect('login')
			
		context = {
            'form':form
        }
		return render(request, 'home/signup.html', context)

def login_page(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'home/login.html', context)