# Generated by Django 2.1.7 on 2019-03-27 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourx', '0002_place_distance'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='map',
            field=models.ImageField(default='/home/insane/PycharmProjects/tourx-website/staticfiles/images', upload_to=''),
        ),
    ]