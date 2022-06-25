from django.urls import path
from . import views
urlpatterns = [
    path('',views.jobs,name='jobs'),
    path('job_details/<str:slug>',views.job_details,name='job_details'),
    path('add_job',views.add_job,name='add_job')
]