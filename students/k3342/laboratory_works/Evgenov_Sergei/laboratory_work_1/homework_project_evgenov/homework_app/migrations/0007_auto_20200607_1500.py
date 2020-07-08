# Generated by Django 3.0.5 on 2020-06-07 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework_app', '0006_auto_20200607_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='importance',
            field=models.CharField(choices=[('высочайшая', 'высочайшая'), ('высокая', 'высокая'), ('средняя', 'средняя'), ('низкая', 'низкая')], max_length=10),
        ),
        migrations.AlterField(
            model_name='comment',
            name='type',
            field=models.CharField(choices=[('вопрос', 'вопрос'), ('найдена ошибка', 'найдена ошибка'), ('иное', 'иное')], max_length=14),
        ),
    ]
