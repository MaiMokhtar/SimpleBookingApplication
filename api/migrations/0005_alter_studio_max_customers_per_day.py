# Generated by Django 4.1.7 on 2023-02-28 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_studio_max_customers_per_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studio',
            name='max_customers_per_day',
            field=models.IntegerField(default=10),
        ),
    ]