# Generated by Django 4.1.7 on 2023-05-09 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UWEflix', '0003_remove_userpurchasehistory_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='representitive',
            name='clubID',
        ),
    ]
