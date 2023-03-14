from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from ojp.models import Jobseeker, Recruiter, Job
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
        # get jobs posted in dictionry 
        jobs = Job.objects.filter(job_title = "SE").values()
        print(jobs)
        return render(request, 'mainfeed/jobseeker_home.html', context={
            "jobs" : jobs
        })


def addjob(request):
    if request.method == 'GET':
        return render(request, 'mainfeed/addjob.html')
    else:
        recruiter_username = request.session['username']
        # find recruiter id from username

        recruiter_id = Recruiter.objects.filter(recruiter_username=recruiter_username).first().recruiter_id


        job_title = request.POST['job_title']
        job_description = request.POST['job_description']
        job_salary = int(request.POST['job_salary'])
        job_type = request.POST['job_type']
        job_category = request.POST['job_category']
        # recruiter_id = request.session['recruiter_id']
        job = Job(job_title=job_title, job_description=job_description, job_salary=job_salary, job_type=job_type, job_category=job_category, job_recruiter_id=recruiter_id)
        job.save()
        return redirect('home')