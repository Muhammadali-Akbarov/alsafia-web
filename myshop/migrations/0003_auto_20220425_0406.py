# Generated by Django 3.2.12 on 2022-04-25 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0002_auto_20220425_0401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image_330x330',
            field=models.ImageField(blank=True, default='images/fpb_1.jpg', upload_to='', verbose_name='330x330'),
        ),
        migrations.AlterField(
            model_name='products',
            name='image_450_200',
            field=models.ImageField(blank=True, default='images/banner_1.jpg', upload_to='', verbose_name='450x200'),
        ),
    ]