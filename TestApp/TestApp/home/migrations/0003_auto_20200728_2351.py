# Generated by Django 3.0.8 on 2020-07-28 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200728_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trn',
            name='vladelets',
            field=models.TextField(default=' ', max_length=60),
        ),
    ]
