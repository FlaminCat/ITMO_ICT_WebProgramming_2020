# Generated by Django 3.0.4 on 2020-05-07 17:37

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_first_app', '0003_auto_20200507_2033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='date_of_birth',
            field=models.DateField(default='1980-01-01'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='username',
            field=models.CharField(default='username', help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
