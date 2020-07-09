# Generated by Django 3.0.4 on 2020-04-18 16:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('leaderboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_type', models.CharField(choices=[('Collaboration', 'Collaboration'), ('Races', 'Races'), ('Other', 'Other')], max_length=20)),
                ('text', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('racer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leaderboard.Racer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Comment',
            },
        ),
    ]
