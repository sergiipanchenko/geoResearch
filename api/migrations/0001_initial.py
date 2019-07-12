# Generated by Django 2.2.3 on 2019-07-11 14:11

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Polygon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('letter', models.CharField(max_length=1)),
                ('color', models.CharField(max_length=13)),
                ('rank', models.IntegerField()),
                ('ascii', models.IntegerField()),
                ('geometry', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
            ],
        ),
    ]