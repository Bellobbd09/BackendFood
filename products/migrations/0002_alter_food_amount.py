# Generated by Django 4.2.5 on 2023-09-24 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]