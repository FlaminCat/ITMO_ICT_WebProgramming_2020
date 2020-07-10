# Generated by Django 3.0.4 on 2020-06-10 09:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tour_name', models.CharField(max_length=50)),
                ('agency', models.CharField(max_length=50)),
                ('tour_descrption', models.TextField()),
                ('time_of_tour', models.DateField()),
                ('payment', models.TextField()),
            ],
            options={
                'verbose_name': 'Tour',
                'verbose_name_plural': 'Tours',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('comment_type', models.CharField(choices=[('вопрос содержания тура', 'вопрос содержания тура'), ('вопрос об условиях оплаты', 'вопрос об условиях оплаты'), ('отзыв', 'отзыв')], max_length=100)),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.Tour')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]