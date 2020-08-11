# Generated by Django 3.1 on 2020-08-11 10:10

from django.db import migrations, models
import job.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0008_job_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(upload_to=job.models.image_upload),
        ),
    ]
