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
        jobs_posted = list(Job.objects.filter(job_recruiter=Recruiter.objects.filter(recruiter_username=username).first()).all().values())
        context = {
            'jobs_posted': jobs_posted
        }
        return render(request, 'mainfeed/recruiter_home.html', context)
    else:
        # get jobs posted in the last 7 days 
        pass


def addjob(request):
    if request.method == 'GET':
        return render(request, 'mainfeed/addjob.html')
    else:
        recruiter_username = request.session['username']
        # find recruiter id from username

        recruiter = Recruiter.objects.filter(recruiter_username=recruiter_username).first()


        job_title = request.POST['job_title']
        job_description = request.POST['job_description']
        job_salary = int(request.POST['job_salary'])
        job_type = request.POST['job_type']
        job_category = request.POST['job_category']

        job = Job.create(job_title, job_description, job_salary, job_type, job_category, recruiter)

        
        return redirect('home')


def job(request, job_id):
    job = Job.objects.filter(job_id=job_id).first()
    if job == None:
        return HttpResponse("job not found")
    else:
        return render(request, 'mainfeed/job.html', {'job': job})
    # return HttpResponse("job found")