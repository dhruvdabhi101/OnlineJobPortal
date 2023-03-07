from django.urls import path
from . import views 

urlpatterns = [
    # for user authentication
    path('',views.index,name=''),
    path('login/', views.login, name='login'),

    # for applicant
    path('register-jobseeker/', views.register_jobseeker, name='register-jobseeker'),
    

    # for recruiter
    path('register-recruiter/', views.register_recruiter, name='register-recruiter'),
    path('logout', views.logout, name='logout') 
]