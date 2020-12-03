# Generated by Django 3.1.3 on 2020-12-03 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0006_onlinebd'),
    ]

    operations = [
        migrations.CreateModel(
            name='smsmayor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=360)),
                ('list_date', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
