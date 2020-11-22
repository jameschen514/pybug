# Generated by Django 2.2.3 on 2019-08-04 20:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0002_auto_20190804_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('O', 'Operator'), ('P', 'Power'), ('R', 'Read'), ('A', 'Administrator')], default='O', max_length=1),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='bug', max_length=20),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='updated',
            field=models.CharField(default=datetime.datetime(2019, 8, 4, 15, 53, 39, 795849), max_length=19),
        ),
    ]
