# Generated by Django 4.0.6 on 2022-09-15 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_player_apg_player_rpg_player_spg_alter_player_ppg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoes',
            name='size',
            field=models.FloatField(null=True),
        ),
    ]