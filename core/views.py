from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView, TemplateView
from django.utils.decorators import method_decorator
from .decorators import *
from .forms import *


# Create your views here.


class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    initial = {'key': 'value'}
    template_name = 'core/user_register.html'

    @method_decorator(unauthenticated_user)
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
        	is_customer = form.cleaned_data.get('is_customer')
        	is_seller = form.cleaned_data.get('is_seller')
        	if is_customer and is_seller is True:
        		messages.info(request, 'User is either Customer or Seller, not both at same time')
        	else:
	            form.save()
	            # username = form.cleaned_data.get('username')
	            email = form.cleaned_data.get('email')
	            messages.success(request, 'Account was created for ' + email)
	            return redirect('core:user-login')
        return render(request, self.template_name, {'form': form})


class LoginView(TemplateView):
    form_class = UserLogin
    initial = {'key': 'value'}
    template_name = 'core/login.html'

    @method_decorator(unauthenticated_user)
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=username, password=password)
        if user is not None:
            login(request, user)
            if request.user.is_seller:
            	return redirect('book:seller-dashboard')
            elif request.user.is_customer:
            	return redirect('book:user-dashboard')
        else:
            messages.info(request, 'Username OR Password is Incorrect')
        return render(request, 'core/login.html', {'form': form})


def UserLogout(request):
    logout(request)
    return redirect('core:user-login')
