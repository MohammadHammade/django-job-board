from django.shortcuts import render
from .models import job

# Create your views here.
def job_list(request):

    #Model QuerySet Instead of db query (select * from job)
    job_list = job.objects.all()
    
    # jobs is the variable that used in template
    #context must be dict
    context = {'jobs':job_list}
    return render(request,'job/job_list.html',context)

def job_details(request, id):
    job_details = job.objects.get(id=id)
    context = {'job': job_details}
    return render(request,'job/job_details.html',context)