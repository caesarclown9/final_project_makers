# Generated by Django 3.1.3 on 2021-03-09 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
