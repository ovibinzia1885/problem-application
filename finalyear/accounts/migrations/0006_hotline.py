# Generated by Django 3.1.3 on 2020-11-27 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_famousplace'),
    ]

    operations = [
        migrations.CreateModel(
            name='hotline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('THana', models.CharField(max_length=100)),
                ('GovtHOspital', models.CharField(max_length=100)),
                ('Firerservice', models.CharField(max_length=100)),
                ('Bus_counter', models.CharField(max_length=100)),
                ('Train_counter', models.CharField(max_length=100)),
            ],
        ),
    ]
