# Generated by Django 2.2 on 2019-04-10 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ide', models.CharField(max_length=200)),
                ('puntaje', models.IntegerField(default=0)),
                ('timer', models.TimeField(default='00:00')),
            ],
        ),
    ]