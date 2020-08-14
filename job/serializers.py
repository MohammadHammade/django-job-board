#get data from django model then convert it to json and return it

from rest_framework import serializers
from .models import job

class job_serializer(serializers.ModelSerializer):
    class Meta:
        model = job
        fields = '__all__'
        