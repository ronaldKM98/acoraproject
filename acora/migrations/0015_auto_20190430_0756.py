# Generated by Django 2.2 on 2019-04-30 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acora', '0014_equipo_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='codigo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='acora.Partida'),
        ),
    ]
