# Generated by Django 2.2.4 on 2021-04-14 03:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20210414_0119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='project_types',
            new_name='project_type',
        ),
        migrations.AddField(
            model_name='project',
            name='end_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]