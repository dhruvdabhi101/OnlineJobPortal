from django.urls import path
from . import views 



urlpatterns = [
    path('home/',views.home,name='home'),

    # recruiter
    path('addjob',views.addjob,name='addjob'),
    path('job/<int:job_id>/',views.job,name='job'),
    
]
