from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Jobseeker, Recruiter 
from django.contrib import messages 
# from .forms import JobSeekerForm, RecruiterForm 


# Create your views here.
def index(request):
    return render(request, "index.html")

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        role = request.POST['role']
        if role == 'job_seeker':
            if Jobseeker.objects.filter(jobseeker_username=username, jobseeker_password=password).exists():
                request.session['username'] = username
                request.session['role'] = role
                return redirect('home')
            else:
                return render(request, 'userauth/login.html', {'error': 'Invalid credentials'})
            
        elif role == 'recruiter':
            if Recruiter.objects.filter(recruiter_username=username, recruiter_password=password).exists():
                request.session['username'] = username
                request.session['role'] = role
                return redirect('home')
            else:
                return render(request, 'userauth/login.html', {'error': 'Invalid credentials'})

    else :
        return render(request, 'userauth/login.html')

def register_recruiter(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            # check if username already exists
            if Recruiter.objects.filter(recruiter_username=username).exists():
                messages.info(request, 'Username already exists')
                return render(request, 'userauth/register_recruiter.html', {'error': 'Username already exists'})
            elif Recruiter.objects.filter(recruiter_email=email).exists(): # check if email already exists
                messages.info(request, 'Email already exists')
                return render(request, 'userauth/register_recruiter.html', {'error': 'Email already exists'})
            else:
                user = Recruiter(recruiter_username=username, recruiter_email=email, recruiter_password=password)
                request.session['username'] = username
                request.session['role'] = 'recruiter'
                user.save()
                return redirect('home')
            
        else:
            return render(request, 'userauth/register_recruiter.html', {'error': 'Passwords do not match'})


    if request.method == 'GET':
        return render(request, 'userauth/register_recruiter.html')
    

def register_jobseeker(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            # check if username already exists
            if Jobseeker.objects.filter(jobseeker_username=username).exists():
                messages.info(request, 'Username already exists')
                return render(request, 'userauth/register_jobseeker.html', {'error': 'Username already exists'})
            elif Jobseeker.objects.filter(jobseeker_email=email).exists(): # check if email already exists
                messages.info(request, 'Email already exists')
                return render(request, 'userauth/register_jobseeker.html', {'error': 'Email already exists'})
            else:
                user = Jobseeker(jobseeker_username=username, jobseeker_email=email, jobseeker_password=password)
                request.session['username'] = username
                request.session['role'] = 'job_seeker'
                user.save()
                return redirect('home')
            
        else:
            return render(request, 'userauth/register_jobseeker.html', {'error': 'Passwords do not match'})


    if request.method == 'GET':
        return render(request, 'userauth/register_jobseeker.html')