# Generated by Django 5.0 on 2024-01-02 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0005_alter_property_brand_alter_property_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='brand',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='property',
            name='size',
            field=models.CharField(max_length=10),
        ),
    ]
