# Generated by Django 2.2 on 2019-04-30 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acora', '0008_equipo_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='idPista',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AddField(
            model_name='equipo',
            name='puntaje',
            field=models.IntegerField(default=0, max_length=200),
        ),
    ]
