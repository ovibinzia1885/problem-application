# Generated by Django 2.0.3 on 2020-11-18 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('public', '0004_auto_20201118_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='homeapplication',
            name='pic',
            field=models.ImageField(default=1.3, upload_to='photo'),
            preserve_default=False,
        ),
    ]
