# Generated by Django 4.1.5 on 2023-01-23 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='description',
            field=models.TextField(max_length=150, verbose_name='Game Description'),
        ),
    ]
