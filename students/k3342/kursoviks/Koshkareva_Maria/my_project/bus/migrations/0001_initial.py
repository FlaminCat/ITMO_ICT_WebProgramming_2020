# Generated by Django 3.0.7 on 2020-06-25 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport', models.CharField(max_length=10)),
                ('job_class', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3)])),
                ('date_begin', models.DateField()),
                ('work_exp', models.IntegerField()),
                ('salary', models.IntegerField()),
            ],
        ),
    ]