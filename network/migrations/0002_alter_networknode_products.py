# Generated by Django 4.2.2 on 2024-09-20 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('network', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networknode',
            name='products',
            field=models.ManyToManyField(to='products.product', verbose_name='продукция'),
        ),
    ]
