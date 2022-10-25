from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        a = reg(request.POST)
        if a.is_valid():
            Name = a.cleaned_data['nme']
            Address = a.cleaned_data['add']
            Email = a.cleaned_data['eml']
            Username = a.cleaned_data['usr']
            Password = a.cleaned_data['psw']
            b = registration(nme=Name, add=Address, eml=Email, usr=Username, psw=Password)
            b.save()
            return HttpResponse("Registeration success")
        else:
            return HttpResponse("Registeration Failed")
    else:
        return render(request, 'regs.html')


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


