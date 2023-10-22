# Generated by Django 4.2.4 on 2023-10-22 20:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recomendacao', '0004_alter_historico_chuva_alter_historico_fosforo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historico',
            name='chuva',
        ),
        migrations.RemoveField(
            model_name='historico',
            name='fosforo',
        ),
        migrations.RemoveField(
            model_name='historico',
            name='nitrogenio',
        ),
        migrations.RemoveField(
            model_name='historico',
            name='ph',
        ),
        migrations.RemoveField(
            model_name='historico',
            name='potassio',
        ),
        migrations.RemoveField(
            model_name='historico',
            name='temperatura',
        ),
        migrations.RemoveField(
            model_name='historico',
            name='umidade',
        ),
        migrations.AddField(
            model_name='historico',
            name='entrada_usuario',
            field=models.JSONField(default={}, null=True),
        ),
        migrations.AlterField(
            model_name='historico',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]