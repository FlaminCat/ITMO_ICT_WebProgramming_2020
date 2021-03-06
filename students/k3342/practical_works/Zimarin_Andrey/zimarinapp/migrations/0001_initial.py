# Generated by Django 2.2 on 2020-09-24 19:07

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
                ('brand', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('number', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.CharField(max_length=20)),
                ('birthday', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Owning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_started', models.DateTimeField(blank=True, null=True)),
                ('date_ended', models.DateTimeField(blank=True, null=True)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zimarinapp.Car')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zimarinapp.Owner')),
            ],
        ),
        migrations.AddField(
            model_name='owner',
            name='owns',
            field=models.ManyToManyField(through='zimarinapp.Owning', to='zimarinapp.Car'),
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_id', models.PositiveIntegerField()),
                ('date', models.DateField(blank=True, null=True)),
                ('type', models.CharField(choices=[('A', 'Bike'), ('B', 'Light Rigid'), ('C', 'Medium Rigid'), ('D', 'Heavy Rigid'), ('E', 'Heavy Combination')], max_length=5)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zimarinapp.Car')),
            ],
        ),
    ]
