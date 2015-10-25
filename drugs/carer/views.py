from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Patient

def index(request):
	template = loader.get_template('carer/index.html')
	return HttpResponse(template.render(template))


# Create your views here.
