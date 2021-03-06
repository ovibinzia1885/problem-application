# Generated by Django 3.1.3 on 2020-12-03 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mayor', '0002_fileadmin_is_published'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfficerMeeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('date', models.DateField(max_length=250)),
                ('time', models.TimeField(max_length=250)),
                ('day', models.CharField(max_length=250)),
                ('seminarroom', models.CharField(choices=[('AB1', 'AB1'), ('BC2', 'BC2'), ('CC3', 'CC3'), ('DD4', 'DD4'), ('EE5', 'EE5')], default='AB1', max_length=10)),
                ('is_published', models.BooleanField()),
            ],
        ),
    ]
