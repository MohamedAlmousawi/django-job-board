from django.shortcuts import redirect, render
from django.urls import reverse
from .models import *
from django.core.paginator import Paginator
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def jobs(request):
    jobs= Job.objects.all()
    paginator = Paginator(jobs, 1) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "jobs": page_obj
    }
    return render(request,'pages/jobs.html',context)

def job_details(request,slug):
    job= Job.objects.get(slug=slug)

    if request.method == "POST":
        form = ApplyForm(request.POST,request.FILES)
        if form.is_valid():
            myform =form.save(commit=False)
            myform.job=job
            myform.save()
    else:
        form = ApplyForm()

    context = {
        'job':job,
        'form':form
    }
    return render(request,'pages/job_details.html',context)

@login_required
def add_job(request):
    if request.method == "POST":
        form = JobForm(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner =request.user
            myform.save()
            return redirect('/')
    else:
        form = JobForm()

    context= {'form':form,
    
    
    }
    return render(request,'pages/add_job.html',context)