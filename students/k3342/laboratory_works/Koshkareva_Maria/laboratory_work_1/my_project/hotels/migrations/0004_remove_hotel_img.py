# Generated by Django 3.0.5 on 2020-04-20 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0003_hotel_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='img',
        ),
    ]
