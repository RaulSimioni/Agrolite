# Generated by Django 4.2.4 on 2023-10-22 21:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recomendacao', '0012_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historico',
            name='data_entrada',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]