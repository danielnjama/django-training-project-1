# Generated by Django 4.2.11 on 2024-04-17 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_category_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='url',
            field=models.SlugField(unique=True),
        ),
    ]
