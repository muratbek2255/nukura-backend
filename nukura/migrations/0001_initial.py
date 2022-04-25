# Generated by Django 4.0.3 on 2022-04-25 11:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155)),
            ],
        ),
        migrations.CreateModel(
            name='NukuraStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(default='image/burger-2.jpg', upload_to='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('author_name', models.CharField(default='Murat', max_length=255)),
                ('categ', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cat', to='nukura.category')),
            ],
        ),
        migrations.CreateModel(
            name='UserStoreRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False)),
                ('in_storemarks', models.BooleanField(default=False)),
                ('rate', models.PositiveSmallIntegerField(choices=[(1, 'OK'), (2, 'FINE'), (3, 'GOOD'), (4, 'AMAZING'), (5, 'INCREDIBLE')])),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nukura.nukurastore')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='nukurastore',
            name='readers',
            field=models.ManyToManyField(related_name='store', through='nukura.UserStoreRelation', to=settings.AUTH_USER_MODEL),
        ),
    ]
