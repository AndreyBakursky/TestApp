# Generated by Django 3.0.8 on 2020-07-29 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persons', '0002_auto_20200729_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='balance',
            field=models.DecimalField(decimal_places=16, max_digits=32),
        ),
    ]
