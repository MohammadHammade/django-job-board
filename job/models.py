from django.db import models

# Create your models here.

# django models field
#     - html widget
#     - validation
#     - db size

    #( to add those Tables And Columns fields to db ) run in terminal
    #1 - python manage.py makemigrations
    #2 - python manage.py migrate
class job(models.Model): # each class equal table in db 
    
    # each field equal column in db 
    #  and django will give:
    #  html widget (input field because charfield) to "title"
    #  validation (input field  <= 100 chars) to "title"
    #  db size in db to "title"
    
    title = models.CharField(max_length=100) 
