# Generated by Django 3.1.3 on 2020-12-05 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0007_smsmayor'),
    ]

    operations = [
        migrations.CreateModel(
            name='notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('date', models.DateField()),
                ('is_published', models.BooleanField()),
                ('list_date', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
