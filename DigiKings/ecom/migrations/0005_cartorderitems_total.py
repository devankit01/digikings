# Generated by Django 3.2.7 on 2021-11-20 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0004_cartorderitems'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorderitems',
            name='Total',
            field=models.FloatField(null=True),
        ),
    ]
