from django.db import models
from django.utils .text import slugify
# Create your models here.

#  using models.Model inheritance , django models field will have a
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

# instance is obj of job class
def image_upload(instance,filename):
    imagename , extension = filename.split(".") 
    return f'jobs/{instance.id}_{imagename}.{extension}'
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
    category = models.ForeignKey('category',on_delete=models.CASCADE,)
    image = models.ImageField(upload_to=image_upload)

    # to make semantic words in urls as the title of the job
    slug = models.SlugField(blank=True,null=True)







    #override the save method
    def save(self, *args,**keywords):
        # code execute before admin click save in admin page
        
        #slagify is method in django apply something on string
        # ex home page => home-page
        self.slug = slugify(self.title)
        
        super(job,self).save(*args,**keywords  )

    # to define object name
    def __str__(self):
        return self.title




class category(models.Model):
    
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class apply(models.Model):
    job = models.ForeignKey(job,related_name='apply_job',on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField()
    cv = models.FileField(upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateField(auto_now=True)

    
    def __str__(self):
        return self.name
    