# Generated by Django 4.1.5 on 2023-01-30 21:02

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0020_delete_shopinfomixin_alter_category_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='game',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Description'),
        ),
    ]