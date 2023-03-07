

from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from django.contrib.auth import login as make_login
from django.core.exceptions import ObjectDoesNotExist

from .forms import CustomUserCreationForm
from .models import UserProfile

# Create your views here.


def registro(request):

    data = {

        'form': CustomUserCreationForm()

    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login(request, user)
            return redirect(to="index")
        data["form"] = formulario


    return render(request, 'registration/registro.html', data)


