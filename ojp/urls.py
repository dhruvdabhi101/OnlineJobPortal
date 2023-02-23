from django.urls import path
from . import views 

urlpatterns = [
    # for user authentication
    path('index/',views.index,name='index'),
    path('register-recruiter/', views.registerRecruiter, name='register-recruiter'),
    path('register-job-seeker/', views.registerJobSeeker, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('forgorpassword/', views.forgotpassword, name='forgotpassword'),
    

    # for applicant
    

    # for recruiter
    
]