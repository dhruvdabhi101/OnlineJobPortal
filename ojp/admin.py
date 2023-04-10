from django.contrib import admin

# Register your models here.
from .models import Jobseeker, Recruiter, Job, Resume, AppliedJob

@admin.register(Jobseeker)
class JobSeekerAdmini(admin.ModelAdmin):
    list_display = ['jobseeker_id', 'jobseeker_username', 'jobseeker_name', 'jobseeker_email', 'jobseeker_phone']


@admin.register(Recruiter)
class Recruiter(admin.ModelAdmin):
    list_display = ['recruiter_id', 'recruiter_username', 'recruiter_email',]

@admin.register(Job)
class Job(admin.ModelAdmin):
    list_display = ['job_id', 'job_title', 'job_description', 'job_salary', 'job_type', 'job_category']

@admin.register(Resume)
class Resume(admin.ModelAdmin):
    list_display = ['address', 'education', 'experience', 'skills']


@admin.register(AppliedJob)
class AppliedJobs(admin.ModelAdmin):
    list_display = ['applied_job_id', 'job_id', 'applied_job_status']




# @admin.register(Job)
# class JobAdmin(admin.ModelAdmin):
#     list_display = [field.name for field in Job._meta.get_fields()]


# @admin.register(Resume)
# class JobSeekerAdmini(admin.ModelAdmin):
#     list_display = [field.name for field in Resume._meta.get_fields()]

# @admin.register(AppliedJob)
# class AppliedJobAdmini(admin.ModelAdmin):
#     list_display = [field.name for field in AppliedJob._meta.get_fields()]