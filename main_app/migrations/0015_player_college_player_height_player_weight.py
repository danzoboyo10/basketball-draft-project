# Generated by Django 4.0.6 on 2022-09-16 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_remove_player_college_player_per_player_player_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='college',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='height',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='weight',
            field=models.CharField(max_length=50, null=True),
        ),
    ]