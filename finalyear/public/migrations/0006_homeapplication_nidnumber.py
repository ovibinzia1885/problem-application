# Generated by Django 2.0.3 on 2020-11-18 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0005_homeapplication_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeapplication',
            name='NIDNumber',
            field=models.CharField(default=2.3, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]