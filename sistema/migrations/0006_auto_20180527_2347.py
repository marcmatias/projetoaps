# Generated by Django 2.0.5 on 2018-05-28 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0005_auto_20180527_2307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estabelecimento',
            name='nome',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
