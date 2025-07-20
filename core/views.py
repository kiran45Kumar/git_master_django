from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request, a):
    return HttpResponse(f"Git is awesome! {a} 😎")

