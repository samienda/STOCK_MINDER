# Generated by Django 5.0 on 2024-01-02 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_alter_purchase_productlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='brand',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='property',
            name='size',
            field=models.CharField(max_length=3),
        ),
    ]
