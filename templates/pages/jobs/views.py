from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator
from .forms import *
# Create your views here.

def jobs(request):
    jobs= Job.objects.all()
    paginator = Paginator(jobs, 2) # Show 25 contacts per page.
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


def add_job(request):
    context = {
    }
    return render(request,'pages/add_job.html',context)