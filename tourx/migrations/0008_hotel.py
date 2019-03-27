# Generated by Django 2.1.7 on 2019-03-27 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourx', '0007_place_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=200)),
                ('picture', models.ImageField(upload_to='maps')),
                ('map', models.ImageField(upload_to='places')),
                ('distance', models.CharField(max_length=10)),
                ('price', models.CharField(max_length=10)),
                ('review', models.CharField(max_length=200)),
            ],
        ),
    ]