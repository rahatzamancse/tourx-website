# Generated by Django 2.1.7 on 2019-03-27 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourx', '0006_place_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='review',
            field=models.CharField(default='Very wonderful place', max_length=200),
            preserve_default=False,
        ),
    ]
