from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def register(request):
    # return render(request, 'userauth/register.html')
    return HttpResponse("Hello, world. You're at the userauth register page.")


def login(request):
    # return render(request, 'userauth/login.html')
    return HttpResponse("Hello, world. You're at the userauth login page.")

def logout(request):
    # return render(request, 'userauth/logout.html')
    return HttpResponse("Hello, world. You're at the userauth logout page.")

def forgotpassword(request):
    # return render(request, 'userauth/forgotpassword.html')
    return HttpResponse("Hello, world. You're at the userauth forgotpassword page.")    