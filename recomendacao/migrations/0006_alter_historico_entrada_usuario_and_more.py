# Generated by Django 4.2.4 on 2023-10-22 21:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recomendacao', '0005_remove_historico_chuva_remove_historico_fosforo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historico',
            name='entrada_usuario',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='historico',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]