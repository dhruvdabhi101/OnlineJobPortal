from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from ojp.models import Jobseeker, Recruiter, Job, Resume, AppliedJob
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
        # get only 5 jobs from database
        jobs = list(Job.objects.all().values())
        context = {
            'jobs': jobs
        }
        return render(request, 'mainfeed/jobseeker_home.html', context)


def addjob(request):
    if request.session['role'] is None:
        return redirect('login')
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

        job = Job.create_job(job_title, job_description, job_salary, job_type, job_category, recruiter)

        
        return redirect('home')


def job(request, job_id):
    if request.session['role'] is None:
        return redirect('login')
    job = Job.objects.filter(job_id=job_id).first()
    if job == None:
        return HttpResponse("job not found")
    else:
        return render(request, 'mainfeed/job.html', {'job': job})
    # return HttpResponse("job found")

def update_job(request,job_id):
    if request.session['role'] is None:
        return redirect('login')
    job = Job.objects.filter(job_id=job_id).first()
    if job == None:
        return HttpResponse("job not found")
    else:
        if request.method == 'GET':
            return render(request, 'mainfeed/update_job.html', {'job': job})
        else:
            try:
                job.update_job(job_id, request.POST['job_title'], request.POST['job_description'], request.POST['job_salary'], request.POST['job_type'], request.POST['job_category'], job.job_recruiter)
            except:
                return HttpResponse("error")
            return redirect('home')
            # if request.POST['job_title']: 
            #     job_title = request.POST['job_title']
            # else:
            #     job_title = job.job_title
            # if request.POST['job_description']:
            #     job_description = request.POST['job_description']
            # else:
            #     job_description = job.job_description
            
            # if request.POST['job_salary']:
            #     job_salary = int(request.POST['job_salary'])
            # else:
            #     job_salary = job.job_salary
            
            # if request.POST['job_type']:
            #     job_type = request.POST['job_type']
            # else:
            #     job_type = job.job_type
            
            # if request.POST['job_category']:
            #     job_category = request.POST['job_category']
            # else:
            #     job_category = job.job_category
            
            # job = Job.update_job(job, job_title, job_description, job_salary, job_type, job_category, job.job_recruiter)
            # return redirect('home')
    
def delete_job(request,job_id):
    job = Job.objects.filter(job_id=job_id).first()
    if job == None:
        return HttpResponse("job not found")
    else:
        job.delete()
        return redirect('home')

def search(request):
    if request.session['role'] is None:
        return redirect('login')
    return render(request, 'mainfeed/searchjob.html')

def search_job(request):
    if request.method == 'POST':
        query = request.POST['search']
        if query == '':
            return render(request, 'mainfeed/searchjob.html')
        jobs = list(Job.objects.filter(job_title__icontains=query).all().values())
        return render(request, 'mainfeed/searchjob.html', {'jobs': jobs})
    else:
        return render(request, 'mainfeed/searchjob.html')

def profile(request):
    if request.session['role'] is None:
        return redirect('login')
    if request.session['role'] == 'recruiter':
        recruiter = Recruiter.objects.filter(recruiter_username=request.session['username']).first()
        context = {
            'recruiter': recruiter
        }
        return render(request, 'mainfeed/recruiter_profile.html', context)
    else:
        jobseeker = Jobseeker.objects.filter(jobseeker_username=request.session['username']).first()
        resume = Resume.objects.filter(jobseeker_id=jobseeker).first()
        context = {
            'jobseeker': jobseeker,
            'resume': resume
        }
        return render(request, 'mainfeed/jobseeker_profile.html', context)

def update_profile(request):
    if request.session['role'] is None:
        return redirect('login')
    else:
        if request.method == 'GET':
            return render(request, 'mainfeed/update_profile.html')
        else:
            if request.session['role'] == 'jobseeker':
                jobseeker = Jobseeker.objects.filter(jobseeker_username=request.session['username']).first()
                jobseeker_id = jobseeker.jobseeker_id
                resume = Resume.objects.filter(jobseeker_id=jobseeker).first()
                address = request.POST['address']
                phone = request.POST['phone_no']
                education = request.POST['education']
                skills = request.POST['skills']
                experience = request.POST['experience']

                if resume == None:
                    jobseeker.update_name(request.POST['name'])
                    jobseeker.update_phone(phone)
                    res = Resume()
                    res = res.create_resume(jobseeker, address, education, experience, skills)

                else:
                    if request.POST['name'] is not "":
                        jobseeker.update_name(request.POST['name'])
                    if phone is not '':
                        jobseeker.update_phone(phone)
                    res = resume.update_resume(jobseeker_id, address, education, experience, skills)
                return redirect('profile')
            else:
                return redirect('profile')
        

def jobseeker(request, username):
    user = Jobseeker.objects.filter(jobseeker_username = username).first()
    resume = Resume.objects.filter(jobseeker_id=user).first()
    return render(request, 'mainfeed/jobseeker.html', {'user': user, 'resume': resume})

def apply(request, job_id):
    if request.session['role'] is None:
        return redirect('login')
    job = Job.objects.filter(job_id=job_id).first()
    jobseeker = Jobseeker.objects.filter(jobseeker_username=request.session['username']).first()
    if job == None and jobseeker == None:
        return HttpResponse("Error")
    else:
        application = AppliedJob()
        application = application.apply_job(jobseeker, job)
        return redirect('home')

    
def update_status(request,application_id):

    application = AppliedJob.objects.filter(applied_job_id=application_id).first()
    # get user from session
    user = Jobseeker.objects.filter(jobseeker_id = application.applied_jobseeker_id).first()
    resume = Resume.objects.filter(jobseeker_id=user).first()
    if application == None and user == None:
        return HttpResponse("Error")
    else:
        if request.method == 'GET':
            return render(request, 'mainfeed/update_status.html', {'user': user, 'resume': resume,  'application': application})
        else:
            status = request.POST['status']
            application.update_status(status)
            return redirect('home')


    # get resume from user

# def delete_applied_job(request, application_id):
#     application = AppliedJob.objects.filter(application_id=application_id).first()
#     if application == None:
#         return HttpResponse("Error")
#     else:
#         application.delete()
#         return redirect('home')

def applied_jobs(request):
    if request.session['role'] is None:
        return redirect('login')
    jobseeker = Jobseeker.objects.filter(jobseeker_username=request.session['username']).first()
    applications = list(AppliedJob.objects.filter(applied_jobseeker=jobseeker).all().values())
    try: 
        for i in applications:
            job = Job.objects.filter(job_id=i['applied_job_id']).first()
            i['job_title'] = job.job_title
            return render(request, 'mainfeed/applied_jobs.html', {'applications': applications})
    except:
        return redirect('home')

def application(request, job_id):
    if request.session['role'] is None:
        return redirect('login')
    job = Job.objects.filter(job_id=job_id).first()
    applications = list(AppliedJob.objects.filter(job_id=job).all().values())
    for i in applications:
        jobseeker = Jobseeker.objects.filter(jobseeker_id=i['applied_jobseeker_id']).first()
        i['jobseeker_name'] = jobseeker.jobseeker_name
        i['jobseeker_username'] = jobseeker.jobseeker_username

    return render(request, 'mainfeed/applications.html', {'applications': applications})