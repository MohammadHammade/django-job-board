from django.contrib import admin

# Register your models here.

# here to add the modelfile to website admin

from .models import job, category ,apply

#the job app will add to website admin
admin.site.register(job)

admin.site.register(category)

admin.site.register(apply)
