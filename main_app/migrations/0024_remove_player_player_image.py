# Generated by Django 4.0.6 on 2022-09-17 02:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0023_alter_player_player_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='player_Image',
        ),
    ]
