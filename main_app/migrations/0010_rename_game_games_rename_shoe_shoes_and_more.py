# Generated by Django 4.0.6 on 2022-08-09 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_rename_shoes_shoe_rename_shoes_player_shoe'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Game',
            new_name='Games',
        ),
        migrations.RenameModel(
            old_name='Shoe',
            new_name='Shoes',
        ),
        migrations.AlterModelOptions(
            name='games',
            options={'ordering': ['-date']},
        ),
        migrations.RenameField(
            model_name='player',
            old_name='shoe',
            new_name='shoes',
        ),
    ]
