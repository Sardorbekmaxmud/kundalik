# Generated by Django 4.2.2 on 2023-06-25 09:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kundalik', '0006_alter_teachermodel_toifa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancemodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='grademodel',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
