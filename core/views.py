from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    a = 'Kiran'
    return HttpResponse(f"Updated: Git is awesome! {a} 😎")

