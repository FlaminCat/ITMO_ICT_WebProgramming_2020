# Generated by Django 3.0 on 2020-06-05 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0008_auto_20200605_2132'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='grade',
            unique_together={('student', 'subject', 'grade')},
        ),
    ]