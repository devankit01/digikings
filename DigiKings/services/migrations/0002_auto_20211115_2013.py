# Generated by Django 3.0.14 on 2021-11-15 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfflineShopSale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CustomerName', models.CharField(blank=True, max_length=200, null=True)),
                ('CustomerPhone', models.CharField(blank=True, max_length=200, null=True)),
                ('CustomerEmail', models.CharField(blank=True, max_length=200, null=True)),
                ('TotalAmount', models.IntegerField(blank=True, default=0, null=True)),
                ('PaidAmount', models.IntegerField(blank=True, default=0, null=True)),
                ('DueAmount', models.IntegerField(blank=True, default=0, null=True)),
                ('isPaid', models.BooleanField(default=False)),
                ('SaleDate', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='teammodel',
            name='ProfilePic',
            field=models.ImageField(upload_to='profile/'),
        ),
    ]
