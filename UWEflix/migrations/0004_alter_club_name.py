# Generated by Django 4.1.5 on 2023-01-14 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        #('main', '0003_address_contact_alter_club_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
