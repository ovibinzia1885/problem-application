# Generated by Django 3.1.3 on 2020-12-04 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0013_auto_20201201_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicfeedback',
            name='problemtype',
            field=models.CharField(default=2.2, max_length=250),
            preserve_default=False,
        ),
    ]
