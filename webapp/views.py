from django.shortcuts import render
from django.http import HttpResponse

def index(request): 
	return HttpResponse("<h2>HEY!</h2>")

def catnote(request): 
	return HttpResponse("<h2>I like cats.</h2>")

def tunanote(request): 
	return HttpResponse("<h1>I like tuna.</h1>")	


# Create your views here.
