# Generated by Django 3.1.3 on 2020-12-01 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20201201_1233'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created',), 'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
    ]