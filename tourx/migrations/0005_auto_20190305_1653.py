# Generated by Django 2.1.7 on 2019-03-05 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourx', '0004_auto_20190305_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth',
            field=models.DateField(default=0),
        ),
    ]