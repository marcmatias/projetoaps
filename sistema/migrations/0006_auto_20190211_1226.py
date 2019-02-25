# Generated by Django 2.0.5 on 2019-02-11 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0005_auto_20190210_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='sala',
            name='estabelecimento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sistema.Estabelecimento'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='consumo',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='estabelecimento',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='predio',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=100),
        ),
        migrations.AlterField(
            model_name='sala',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=100),
        ),
    ]
