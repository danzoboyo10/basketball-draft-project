# Generated by Django 4.0.6 on 2022-07-12 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_games_options_alter_games_game'),
    ]

    operations = [
        migrations.AlterField(
            model_name='games',
            name='game',
            field=models.CharField(choices=[('A', 'Away'), ('H', 'Home'), ('P', 'Playoffs')], default='A', max_length=1),
        ),
    ]
