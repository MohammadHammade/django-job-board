# Generated by Django 3.1 on 2020-08-14 15:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info',
            old_name='palce',
            new_name='place',
        ),
    ]
