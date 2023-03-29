from django.urls import path
from . import views 



urlpatterns = [
    path('home/',views.home,name='home'),

    # recruiter
    path('addjob',views.addjob,name='addjob'),
    path('job/<int:job_id>/',views.job,name='job'),
    path('update_job/<int:job_id>',views.update_job,name='update_job'),
    path('delete_job/<int:job_id>',views.delete_job,name='delete_job'),

    # jobseeker
    path('search_job', views.search_job, name='search_job'),
    
]
