# Generated by Django 4.0.3 on 2022-05-15 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_ecocompany_company_eco_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.CharField(default='Gogolya 123', max_length=100),
        ),
    ]
