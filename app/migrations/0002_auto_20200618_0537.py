# Generated by Django 3.0.7 on 2020-06-18 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shorturl',
            name='long_url',
            field=models.CharField(max_length=200),
        ),
    ]
