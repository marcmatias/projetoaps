# Generated by Django 2.0.5 on 2018-05-31 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consumo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100)),
                ('kwh', models.FloatField()),
                ('data', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Predio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100)),
                ('predio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.Predio')),
            ],
        ),
        migrations.AddField(
            model_name='consumo',
            name='predio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.Predio'),
        ),
        migrations.AddField(
            model_name='consumo',
            name='sala',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sistema.Sala'),
        ),
        migrations.AlterUniqueTogether(
            name='sala',
            unique_together={('predio', 'nome')},
        ),
        migrations.AlterUniqueTogether(
            name='consumo',
            unique_together={('sala', 'data')},
        ),
    ]