# Generated by Django 3.1.5 on 2021-01-22 18:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_auto_20210122_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webaddress',
            name='validity_term',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 23, 18, 5, 32, 762876)),
        ),
    ]
