from django.shortcuts import render,redirect
from .models import job
from django.core.paginator import Paginator
from django.shortcuts import render
from .form import apply_form ,job_form
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from .filter import JobFilter

# Create your views here.
def job_list(request):

    #Model QuerySet Instead of db query (select * from job)
    job_list = job.objects.all()
    
    #filter
    # the info returned from GET 
    # apply returned filter info on job_list witch has all jobs
    myfilter = JobFilter(request.GET,queryset=job_list)
    
    # the result on filter will be in job_list
    # qs = queryset
    job_list = myfilter.qs


    #for pagination
    n = 2
    paginator = Paginator(job_list,n) #show n page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    # jobs is the variable that used in template
    #context must be dict
    # we send myfilter to show what type of filter done
    context = {'jobs':job_list,'page':page_obj,'myfilter':myfilter }
    return render(request,'job/job_list.html',context)

def job_details(request, slug):
    job_details = job.objects.get(slug=slug)

    # if applyjob is clicked 
    if request.method == 'POST':
        # the returned data will be in request.POST
        # the uploaded file and image will be in request.FIELS
        form = apply_form(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job =job_details
            myform = form.save()
            
    # no supplied datqa >> just show the form page 
    else:
        form = apply_form()


    context = {'job': job_details,'form':form}
    return render(request,'job/job_detail.html',context)


# decorator to make this function deosnt work without login
@login_required
def add_job(request):
    if request.method == "POST":
        form = job_form(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user #loginned user
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form = job_form()
    return render(request,'job/add_job.html',{'form':form})


