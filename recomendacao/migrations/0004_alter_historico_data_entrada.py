# Generated by Django 4.2.4 on 2023-10-23 02:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recomendacao', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historico',
            name='data_entrada',
            field=models.DateTimeField(verbose_name=django.utils.timezone.now),
        ),
    ]
