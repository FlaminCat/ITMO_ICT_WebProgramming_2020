# Generated by Django 2.2 on 2020-09-24 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zimarinapp', '0002_auto_20200924_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zimarinapp.Owner'),
        ),
    ]