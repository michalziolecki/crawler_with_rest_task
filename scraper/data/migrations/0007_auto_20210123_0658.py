# Generated by Django 3.1.5 on 2021-01-23 06:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_auto_20210122_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webaddress',
            name='validity_term',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
