from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm

# Create your views here.


def home(request):
    numbers = [1,2,3,4,5]
    name = 'Max Goodridge'
    args = {'myName': name, 'numbers': numbers}
    return render(request, 'accounts/home.html', args)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account')

    else:
        form = RegistrationForm()

        args = {'form': form}
        return render (request, 'accounts/reg_form.html', args)
