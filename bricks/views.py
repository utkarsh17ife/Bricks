from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm
from .forms import SigninForm


def index(request):
	if request.user.is_authenticated:
		return render(request, 'home_user.html')
	else:
		return render(request, 'home.html')

def signin(request):
	if request.user.is_authenticated:
		return redirect('/')
	elif request.method == 'POST':
		form = SigninForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return render(request, 'home_user.html')
		else:
			return HttpResponse(form.errors.as_json())
	return render(request, 'signin.html')

def signup(request):
	if request.user.is_authenticated:
		return redirect('/')
	elif request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			email = request.POST['email']
			password = request.POST['password']
			user = User.objects.create_user(username, email, password)

			user.first_name = request.POST['first_name']
			user.last_name = request.POST['last_name']
			user.userinfo.city = request.POST['city']
			user.userinfo.state = request.POST['state']
			user.userinfo.zip = request.POST['zip']
			user.userinfo.phone = request.POST['phone']
			user.save()
			return HttpResponse('success. Go and sign in')
		else:
			return HttpResponse(form.errors.as_json())
	return render(request, 'signup.html')

def signout(request):
	logout(request)
	return redirect('/')