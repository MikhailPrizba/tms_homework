# Generated by Django 4.1.5 on 2023-01-23 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0004_alter_game_release_date_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='release_date_at',
            field=models.DateTimeField(verbose_name='Release date'),
        ),
    ]
