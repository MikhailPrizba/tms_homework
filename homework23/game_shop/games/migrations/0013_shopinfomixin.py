# Generated by Django 4.1.5 on 2023-01-29 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0012_category_games_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopInfoMixin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
