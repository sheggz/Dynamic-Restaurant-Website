# Generated by Django 4.1.3 on 2023-10-07 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='Description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='menu',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
