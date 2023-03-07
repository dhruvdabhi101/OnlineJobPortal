from django.forms import ModelForm 
from .models import Jobseeker, Recruiter

class JobSeekerForm(ModelForm):
    class Meta:
        model = Jobseeker
        fields = ['jobseeker_username', 'jobseeker_email', 'jobseeker_password']


class RecruiterForm(ModelForm):
    class Meta:
        model = Recruiter
        fields = ['recruiter_username', 'recruiter_email', 'recruiter_password']