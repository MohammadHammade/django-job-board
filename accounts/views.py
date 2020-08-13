from django.shortcuts import render,redirect
from .forms import signup_form ,user_form,profile_form
from django.contrib.auth import authenticate,login
from django.urls import reverse
from .models import profile as pro

# Create your views here.

def signup(request):
    if request.method == "POST":
        #save form  data
        form = signup_form(request.POST)
        if form.is_valid:
            
            # save form data
            form.save()

            # logged in after save
            
            user_name = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #check if user_name,password are exist in db
            user = authenticate(username=user_name, password=password)

            #Login
            login(request,user)
            return redirect('/accounts/profile')
        else:
            pass
    else:
        # show form
        form = signup_form()
    return render(request,'registration/signup.html',{'form':form})


def profile(request):
    # get current user
    profile_user = pro.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile':profile_user})


def profile_edit(request):
    profile_user = pro.objects.get(user=request.user)
    
    if request.method == "POST":
    
        #to save returned data from request.POST
        # request.FILES to edit new image
        # intance to pass user data to show it i n forms
        
        userform = user_form(request.POST,instance=request.user)
        profileform = profile_form(request.POST,request.FILES,instance=profile_user)
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            
            # to determine witch user to edit
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect(reverse('accounts:profile'))

    else:   
        #show forms and 
        # intance to pass user data to show it in forms
        userform = user_form(instance=request.user)
        profileform = profile_form(instance=profile_user)
        
    return render(request,'accounts/profile_edit.html',{'userform':userform,'profileform':profileform})
