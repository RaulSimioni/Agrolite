# Generated by Django 4.2.4 on 2023-11-24 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recomendacao', '0005_alter_historico_data_entrada'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historico',
            name='data_entrada',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]