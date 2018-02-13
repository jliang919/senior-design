# Generated by Django 2.0.1 on 2018-02-12 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('senior_des', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='room_number',
            field=models.IntegerField(default='-1'),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='is_occupied',
            field=models.BooleanField(),
        ),
    ]
