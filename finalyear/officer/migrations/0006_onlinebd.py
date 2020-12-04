# Generated by Django 3.1.3 on 2020-12-02 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officer', '0005_auto_20201201_2330'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnlineBd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='media')),
                ('PersonalNumber', models.CharField(max_length=17, unique=True)),
                ('BithofDate', models.CharField(max_length=100)),
                ('is_published', models.BooleanField()),
                ('list_date', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-list_date',),
            },
        ),
    ]