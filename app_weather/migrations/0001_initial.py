# Generated by Django 4.0 on 2021-12-28 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WindData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='date published')),
                ('wind_speed', models.FloatField(max_length=200)),
                ('wind_direction', models.FloatField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TemperatureData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(max_length=200)),
                ('feels_like', models.FloatField(max_length=200)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_weather.winddata')),
            ],
        ),
        migrations.CreateModel(
            name='OtherWeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pressure', models.FloatField(max_length=200)),
                ('humidity', models.FloatField(max_length=200)),
                ('visibility', models.FloatField(max_length=200)),
                ('sky', models.CharField(max_length=200)),
                ('main', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('sunrise', models.CharField(max_length=200)),
                ('sunset', models.CharField(max_length=200)),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_weather.winddata')),
            ],
        ),
    ]
