# Generated by Django 4.1.5 on 2023-02-01 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0021_alter_category_description_alter_game_description'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='game',
            index=models.Index(fields=['title'], name='games_game_title_b7a574_idx'),
        ),
    ]
