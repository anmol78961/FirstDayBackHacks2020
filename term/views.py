from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        pass
    else:
        messages.info(
            request, "You must be Signed-up or Login to play the game")
    return render(request, "term/index.html")


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/user-registration.html', context)


def levels(request):
    return render(request, "term/level.html")
