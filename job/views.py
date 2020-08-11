from django.shortcuts import render
from .models import job
from django.core.paginator import Paginator
from django.shortcuts import render
from .form import apply_form

# Create your views here.
def job_list(request):

    #Model QuerySet Instead of db query (select * from job)
    job_list = job.objects.all()
    
    #for pagination
    n = 1
    paginator = Paginator(job_list,n) #show n page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # jobs is the variable that used in template
    #context must be dict
    context = {'jobs':job_list,'page':page_obj }
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