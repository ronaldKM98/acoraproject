# Generated by Django 2.2 on 2019-04-30 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acora', '0005_auto_20190430_0716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo',
            name='codigo',
        ),
    ]
