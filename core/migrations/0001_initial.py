# Generated by Django 3.0.5 on 2020-05-19 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataStamp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('temperature', models.DecimalField(decimal_places=1, max_digits=3)),
                ('wind_speed', models.DecimalField(decimal_places=1, max_digits=3)),
                ('wind_direction', models.CharField(choices=[('W', 'West'), ('E', 'East'), ('N', 'North'), ('S', 'South'), ('SE', 'SouthEast'), ('SW', 'SouthWest'), ('NE', 'NorthEast'), ('NW', 'NorthWest')], max_length=2)),
                ('pressure', models.IntegerField()),
                ('humidity', models.IntegerField()),
                ('rain_1h', models.IntegerField()),
            ],
        ),
    ]