from audioop import reverse
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect, render
from .forms import *
# Create your views here.
from .models import *
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile')
    else:
        form =SignupForm()
    context = {
        "form":form
    }
    return render(request,'registration/signup.html',context)


def profile(request):
    profile = Profile.objects.get(username=request.user)
    return render(request,'accounts/profile.html',{'profile':profile})

def profile_edit(request):
    profile = Profile.objects.get(username=request.user)
    if request.method == 'POST':
        userform = UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST,request.FILES,instance=profile)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.username = request.user
            myprofile.save()

    else:
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)


    return render(request,'accounts/edit.html',{'userform':userform,'profileform':profileform})