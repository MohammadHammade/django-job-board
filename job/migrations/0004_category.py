# Generated by Django 3.1 on 2020-08-10 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_auto_20200809_2325'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
    ]
