# Generated by Django 3.2.7 on 2021-11-16 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item_Quality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item_quality', models.CharField(choices=[('First Hand', 'First Hand'), ('Second Hand', 'Second Hand')], max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='orders',
            name='Status',
            field=models.CharField(choices=[('ordered', 'ordered'), ('order_confirmed', 'order_confirmed'), ('out for delivery', 'out for delivery'), ('Order Recieved', 'Order Recieved'), ('Order Reject', 'Order Reject')], max_length=200),
        ),
        migrations.AlterField(
            model_name='orders',
            name='quantity',
            field=models.IntegerField(max_length=5),
        ),
        migrations.AlterField(
            model_name='product',
            name='Item_quality',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecom.item_quality'),
        ),
    ]