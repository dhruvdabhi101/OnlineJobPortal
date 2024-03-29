from django.db import models
from django.contrib import admin

# Create your models here.
class Jobseeker(models.Model):
    jobseeker_id = models.AutoField(primary_key=True, default=1)
    jobseeker_username = models.CharField(max_length=50, default="abc")
    jobseeker_name = models.CharField(max_length=50, null=True)
    jobseeker_email = models.CharField(max_length=50, default="default")
    jobseeker_password = models.CharField(max_length=50, default="default")
    jobseeker_phone = models.CharField(max_length=50, null=True)

    def update_phone(self, phone):
        self.jobseeker_phone = phone
        self.save()
    def update_name(self, name):
        self.jobseeker_name = name
        self.save()

    def __str__(self):
        return self.jobseeker_name
    

class Recruiter(models.Model):
    recruiter_id = models.AutoField(primary_key=True, default=1)
    recruiter_username = models.CharField(max_length=50, default="abc")
    recruiter_name = models.CharField(max_length=50, null=True)
    recruiter_email = models.CharField(max_length=50, default="default")
    recruiter_password = models.CharField(max_length=50, default="default")
    recruiter_phone = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.recruiter_name
    


class Job(models.Model):
    job_id = models.AutoField(primary_key=True)
    job_title = models.CharField(max_length=50, null=True)
    job_description = models.CharField(max_length=50, null=True)
    job_salary = models.CharField(max_length=50, null=True)
    job_type = models.CharField(max_length=50, null=True)
    job_category = models.CharField(max_length=50, null=True)
    job_recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)

    def __str__(self):
        if self.job_id == None:
            return "job"
        else:
            return str(self.job_id)
    

    def create_job(title, description, salary, type, category, recruiter):
        job = Job(job_title=title, job_description=description, job_salary=salary, job_type=type, job_category=category, job_recruiter=recruiter)
        job.save()
        return job
    
    def update_job(job, title, description, salary, type, category, recruiter):
        job = Job.objects.get(job_id=job)
        if title:
            job.job_title = title
        if description:
            job.job_description = description
        if salary:
            job.job_salary = salary
        if type:
            job.job_type = type
        if category:
            job.job_category = category
        if recruiter:
            job.job_recruiter = recruiter
        job.save()
        return job

    def delete_job(job_id):
        job = Job.objects.get(job_id=job_id)
        job.delete()
        return job



class AppliedJob(models.Model):
    applied_job_id = models.AutoField(primary_key=True)
    applied_jobseeker = models.ForeignKey(Jobseeker, on_delete=models.CASCADE)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    applied_job_status = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.applied_job_status
    
    def apply_job(self,jobseeker, job, status="Applied"):
        applied_job = AppliedJob(applied_jobseeker=jobseeker, job_id=job, applied_job_status=status)
        applied_job.save()
        return applied_job

    def update_status(self, status):
        self.applied_job_status = status
        self.save()
        return self
    
    def delete(jobseeker, job):
        applied_job = AppliedJob.objects.get(applied_jobseeker=jobseeker, job_id=job)
        applied_job.delete()
        return applied_job

    def search_jobseeker(jobseeker):
        applied_job = AppliedJob.objects.filter(applied_jobseeker=jobseeker)
        return applied_job
    
    def search_job(job):
        applied_job = AppliedJob.objects.filter(job_id=job)
        return applied_job
    

class Resume(models.Model):
    jobseeker_id = models.ForeignKey(Jobseeker, on_delete=models.CASCADE)
    address = models.CharField(max_length=50, null=True)
    education = models.CharField(max_length=50, null=True)
    experience = models.CharField(max_length=50, null=True)
    skills = models.CharField(max_length=50 , null=True)
    resume = models.FileField(upload_to='resume/', null=True)
    def __str__(self):
        return self.address

    def create_resume(self, jobseeker, address, education, experience, skills):
        resume = Resume(jobseeker_id=jobseeker, address=address, education=education, experience=experience, skills=skills)
        resume.save()
        return

    def update_resume(self, jobseeker, address, education, experience, skills):
        if address:
            self.address = address
        if education:
            self.education = education
        if experience:
            self.experience = experience
        if skills:
            self.skills = skills
        self.save()
   