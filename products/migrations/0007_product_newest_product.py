# Generated by Django 5.0.6 on 2024-07-23 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_sizevariant_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='newest_product',
            field=models.IntegerField(default=0),
        ),
    ]
