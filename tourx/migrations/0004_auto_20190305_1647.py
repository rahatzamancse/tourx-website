# Generated by Django 2.1.7 on 2019-03-05 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourx', '0003_auto_20190305_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo_id',
            field=models.ImageField(blank=True, null=True, upload_to='photo_ids', verbose_name='Photo ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profiles', verbose_name='Profile Picture'),
        ),
    ]