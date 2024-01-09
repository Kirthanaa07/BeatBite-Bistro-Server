# Generated by Django 4.1.3 on 2024-01-08 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BeatBiteBistroapi', '0002_alter_customer_phone_number_alter_item_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='default_image.jpg', max_length=50, upload_to=''),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='John Doe', max_length=50),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='Cashier', max_length=50),
        ),
    ]
