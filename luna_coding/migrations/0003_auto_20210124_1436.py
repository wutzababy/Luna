# Generated by Django 3.1.5 on 2021-01-24 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luna_coding', '0002_auto_20210123_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo_profile',
            field=models.ImageField(blank=True, default='default_profile.png', null=True, upload_to='photo_profile'),
        ),
    ]
