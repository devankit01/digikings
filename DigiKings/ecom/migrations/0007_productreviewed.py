# Generated by Django 3.2.7 on 2021-11-20 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20211111_1410'),
        ('ecom', '0006_alter_orders_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductReviewed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.TextField()),
                ('review_rating', models.CharField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], max_length=150)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile')),
            ],
        ),
    ]
