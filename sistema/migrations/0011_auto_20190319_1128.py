# Generated by Django 2.0.5 on 2019-03-19 14:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0010_auto_20190319_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumo',
            name='data',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
