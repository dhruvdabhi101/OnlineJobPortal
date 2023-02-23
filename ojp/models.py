from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    image = models.ImageField(upload_to="Applicants/uploads/")
    gender = models.CharField(max_length=10)
    type = models.CharField(max_length=15)
    password = models.CharField(max_length=20)
 
    def __str__(self):
        return self.user.first_name

class Recruiter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    image = models.ImageField(upload_to="Recruiters/uploads/")
    gender = models.CharField(max_length=10)
    company_name = models.CharField(max_length=50)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.user.first_name
    
class Job(models.Model):
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=50)
    salary = models.IntegerField()
    experience = models.IntegerField()
    skills = models.CharField(max_length=100)
    vacancies = models.IntegerField()
    type = models.CharField(max_length=10)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    
class Applied(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    status = models.CharField(max_length=10)

    def __str__(self):
        return self.job.title + " - " + self.applicant.user.first_name