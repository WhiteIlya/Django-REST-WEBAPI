# Generated by Django 4.1.3 on 2024-03-19 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0002_item_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image_url',
            field=models.CharField(default='', max_length=255),
        ),
    ]