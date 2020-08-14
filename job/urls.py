from django.urls import path,include

from . import views
from . import api

app_name = 'job'

urlpatterns = [
    path('',views.job_list,name = "job_list"),
    path('add',views.add_job,name='add_job'),
    path('<str:slug>',views.job_details,name='job_detail'),

    #api
    path('api/list',api.job_list_api,name='job_list_api'),
]