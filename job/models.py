from django.db import models

# Create your models here.

# django models field will have a
#     - html widget
#     - validation
#     - db size


    #( to add those Tables And Columns fields to db ) run in terminal
    #1 - python manage.py makemigrations
    #2 - python manage.py migrate

JOB_TYPE = (
    ('Full TIme','Full TIme'),
    ('Part Time','Part TIme'),
)
class job(models.Model): # each class equal table in db 
    
    # each field equal column in db 
    #  and django will give:
    #  html widget (input field because charfield) to "title"
    #  validation (input field  <= 100 chars) to "title"
    #  best db column datatype to "title"
    
    title = models.CharField(max_length=100)
    # location
    job_type = models.CharField(max_length=15,choices=JOB_TYPE)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)

    # to define object name
    def __str__(self):
        return self.title