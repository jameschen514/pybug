# Generated by Django 2.2 on 2020-05-04 19:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0009_auto_20200429_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='attachment',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='updated',
            field=models.CharField(default=datetime.datetime(2020, 5, 4, 15, 39, 26, 379150), max_length=19),
        ),
    ]