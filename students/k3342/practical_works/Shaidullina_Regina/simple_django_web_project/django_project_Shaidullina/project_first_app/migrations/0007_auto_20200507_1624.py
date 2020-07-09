# Generated by Django 3.0.4 on 2020-05-07 13:24

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0006_auto_20200507_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='birth_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='owner',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
