# Generated by Django 3.0.8 on 2020-07-28 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200728_2351'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Trn',
            new_name='Clients',
        ),
        migrations.AlterModelOptions(
            name='clients',
            options={'verbose_name': 'Клиент ТестБанка', 'verbose_name_plural': 'Клиенты ТестБанка'},
        ),
    ]