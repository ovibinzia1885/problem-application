# Generated by Django 3.1.3 on 2020-12-03 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mayor', '0004_remove_officermeeting_seminarroom'),
    ]

    operations = [
        migrations.AddField(
            model_name='officermeeting',
            name='roomno',
            field=models.CharField(default='ovi', max_length=6),
        ),
    ]
