# Generated by Django 4.0.3 on 2022-05-13 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='phone_number',
            field=models.IntegerField(unique=True),
        ),
    ]
