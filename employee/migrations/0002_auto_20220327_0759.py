# Generated by Django 3.2.6 on 2022-03-27 02:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='Data1',
            new_name='data1',
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='Data2',
            new_name='data2',
        ),
    ]