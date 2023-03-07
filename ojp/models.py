from django.db import models

# Create your models here.
class Jobseeker(models.Model):
    jobseeker_id = models.AutoField(primary_key=True, default=1)
    jobseeker_username = models.CharField(max_length=50, default="abc")
    jobseeker_name = models.CharField(max_length=50, null=True)
    jobseeker_email = models.CharField(max_length=50, default="default")
    jobseeker_password = models.CharField(max_length=50, default="default")
    jobseeker_phone = models.CharField(max_length=50, null=True)

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
    job_id = models.AutoField(primary_key=True, default=1)
    job_title = models.CharField(max_length=50, null=True)
    job_description = models.CharField(max_length=50, null=True)
    job_salary = models.CharField(max_length=50, null=True)
    job_type = models.CharField(max_length=50, null=True)
    job_category = models.CharField(max_length=50, null=True)
    job_recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)

    def __str__(self):
        return self.job_title
    


class AppliedJob(models.Model):
    applied_job_id = models.AutoField(primary_key=True)
    applied_jobseeker = models.ForeignKey(Jobseeker, on_delete=models.CASCADE)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    applied_job_status = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.applied_job_status
    

class Resume(models.Model):
    jobseeker_id = models.ForeignKey(Jobseeker, on_delete=models.CASCADE)
    address = models.CharField(max_length=50, null=True)
    education = models.CharField(max_length=50, null=True)
    experience = models.CharField(max_length=50, null=True)
    skills = models.CharField(max_length=50 , null=True)
    resume = models.FileField(upload_to='resume/', null=True)
    def __str__(self):
        return self.address