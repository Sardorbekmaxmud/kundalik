# Generated by Django 4.2.2 on 2023-06-25 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kundalik', '0003_alter_schoolmodel_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classmodel',
            name='name',
            field=models.CharField(default='', max_length=4),
        ),
    ]