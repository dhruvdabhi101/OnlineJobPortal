from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from ojp.models import Jobseeker, Recruiter
from django.contrib import messages 
from django.http import HttpResponse
 
def home(request):
    username = request.session['username']
    role = request.session['role']
    if role == None:
        return redirect('login')
    elif role == 'recruiter':
        return render(request, 'mainfeed/recruiter_home.html')
    else:
        return render(request, 'mainfeed/jobseeker_home.html')