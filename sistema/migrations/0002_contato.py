# Generated by Django 2.0.5 on 2018-06-20 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]