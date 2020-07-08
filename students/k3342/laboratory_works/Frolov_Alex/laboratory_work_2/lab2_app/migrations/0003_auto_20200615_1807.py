# Generated by Django 3.0.5 on 2020-06-15 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab2_app', '0002_auto_20200613_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nclass',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='klass', to='lab2_app.Teacher'),
        ),
        migrations.AlterField(
            model_name='room',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room', to='lab2_app.Teacher'),
        ),
        migrations.AlterField(
            model_name='timetable',
            name='nclass_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timetable', to='lab2_app.Nclass'),
        ),
    ]
