# Generated by Django 2.0.6 on 2020-05-20 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_auto_20200520_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='number',
            field=models.CharField(max_length=3, primary_key=True, serialize=False),
        ),
    ]
