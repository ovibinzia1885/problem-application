# Generated by Django 3.1.3 on 2020-11-29 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_hotline'),
    ]

    operations = [
        migrations.CreateModel(
            name='recentlysolveproblem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('applicatename', models.CharField(max_length=250)),
                ('wardno', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=250)),
                ('location', models.CharField(max_length=250)),
            ],
        ),
    ]
