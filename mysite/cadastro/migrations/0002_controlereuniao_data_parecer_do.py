# Generated by Django 4.2.1 on 2023-06-02 19:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='controlereuniao',
            name='data_parecer_do',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Data Parecer D.O.'),
        ),
    ]
