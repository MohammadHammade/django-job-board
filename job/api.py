#views like django views but view for api 
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import job
from .serializers import job_serializer

#view need url

@api_view(['GET'])
def job_list_api(request):
    all_jobs = job.objects.all()
    
    #make all jobs as json using serializer
    data = job_serializer(all_jobs,many=True).data
    return Response({'data':data})