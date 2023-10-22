# Generated by Django 4.2.4 on 2023-10-22 21:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recomendacao', '0007_rename_historico_historico_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora', models.DateTimeField(auto_now_add=True)),
                ('nitrogenio', models.FloatField()),
                ('fosforo', models.FloatField()),
                ('potassio', models.FloatField()),
                ('ph', models.FloatField()),
                ('chuva', models.FloatField()),
                ('umidade', models.FloatField()),
                ('temperatura', models.FloatField()),
                ('resposta_ia', models.CharField(max_length=255)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Historico_Usuario',
        ),
    ]