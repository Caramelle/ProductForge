from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Patient
from .forms import RegisterForm


# Create your views here.

def home(request):
    title='Home'
    context = {
        "title": title
    }
    template = loader.get_template('patient/patient_home.html')
    return render(request, "patient/patient_home.html", context)

def register(request):
    form = RegisterForm()
    title='Register'
    context = {
        "title": title,
        "form": form
    }
    return render(request,"patient/register.html",context)



