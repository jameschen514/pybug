# Generated by Django 2.2.3 on 2019-08-04 22:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_auto_20190804_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='updated',
            field=models.CharField(default=datetime.datetime(2019, 8, 4, 17, 24, 38, 197407), max_length=19),
        ),
        migrations.AlterField(
            model_name='user',
            name='firstname',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastname',
            field=models.CharField(max_length=20),
        ),
    ]