from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def login(request):
    return render(request, 'userauth/login.html')

def register_recruiter(request):
    return render(request, 'userauth/register_recruiter.html')

def register_jobseeker(request):
    return render(request, 'userauth/register_jobseeker.html')