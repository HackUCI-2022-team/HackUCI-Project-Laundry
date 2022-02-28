from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm, LaundryForm, DryerForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Floor, Laundry, Dryer

def pre_home_page(request):
    return render(request, 'home/index.html', {})

def create_floor_if_not_exist(floor_id, floor_key):
    try:
        new_floor = Floor()
        new_floor.id = floor_id
        new_floor.floor_key = floor_key
        new_floor.save()
        print(new_floor)
    except Exception as e:
        print("floor wasn't created, probably exists already, err msg:", e)

@login_required(login_url='login')
def home_page(request):
    #user_profiles = UserProfile.objects.filter(floor_key=request.user.floor_key)
    laundry_machines = Laundry.objects.filter(floor_key=request.user.floor_key)
    dryer_machines = Dryer.objects.filter(floor_key=request.user.floor_key)
    
    context = {
        'laundry_machines': laundry_machines,
        'dryer_machines': dryer_machines
    }
    return render(request, 'home/home.html', context)

def signup_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = SignUpForm()
        if request.method == 'POST':
            form = SignUpForm(request.POST)
            if form.is_valid():
                floor_key = form.cleaned_data.get('floor_key')
                create_floor_if_not_exist(floor_key, floor_key)
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

@login_required(login_url='login')
def logout_page(request):
    logout(request)
    return redirect('prehome')

@login_required(login_url='login')
def update_laundry(request, pk):
    laundry = Laundry.objects.filter(floor_key=request.user.floor_key)[pk]
    form = LaundryForm(instance=laundry)

    if request.method == 'POST':
        form = LaundryForm(request.POST, instance=laundry)
        if form.is_valid():
            if form.fields['mode'] != 'neutral':
                laundry.user = request.user
                laundry.save()
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'home/update_laundry.html', context)

@login_required(login_url='login')
def update_dryer(request, pk):
    dryer = Dryer.objects.filter(floor_key=request.user.floor_key)[pk]
    form = DryerForm(instance=dryer)
    
    if request.method == 'POST':
        form = DryerForm(request.POST, instance=dryer)
        if form.is_valid():
            if form.fields['mode'] != 'neutral':
                dryer.user = request.user
                dryer.save()
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'home/update_dryer.html', context)
