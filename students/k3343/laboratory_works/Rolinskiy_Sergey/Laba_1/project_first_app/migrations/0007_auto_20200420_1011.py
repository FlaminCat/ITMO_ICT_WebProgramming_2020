# Generated by Django 3.0.4 on 2020-04-20 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0006_auto_20200420_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='datein',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='dateout',
        ),
    ]
