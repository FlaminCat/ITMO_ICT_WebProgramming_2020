# Generated by Django 3.0.4 on 2020-04-18 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_number', models.CharField(max_length=6)),
                ('description', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Car',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=30)),
                ('number_of_racers', models.IntegerField()),
            ],
            options={
                'db_table': 'Team',
            },
        ),
        migrations.CreateModel(
            name='Racer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('middlename', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=30)),
                ('racer_class', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leaderboard.Car')),
                ('team_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leaderboard.Team')),
            ],
            options={
                'db_table': 'Racer',
            },
        ),
        migrations.CreateModel(
            name='Race',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('category', models.CharField(choices=[('OW', 'Open-wheel racing'), ('TC', 'Touring car racing'), ('SpC', 'Sports car racing'), ('PC', 'Production-car racing'), ('OM', 'One-make racing'), ('TAS', 'Time Attack Series'), ('StC', 'Stock car racing'), ('R', 'Rallying'), ('D', 'Drag racing'), ('OR', 'Off-road racing'), ('K', 'Kart racing'), ('H', 'Historical racing'), ('Other', 'Other')], max_length=5)),
                ('date', models.DateField()),
                ('winner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leaderboard.Racer')),
            ],
            options={
                'db_table': 'Race',
            },
        ),
    ]