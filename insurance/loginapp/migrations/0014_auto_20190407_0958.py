# Generated by Django 2.1.7 on 2019-04-07 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0013_auto_20190407_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(blank=True, default='place', max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.CharField(blank=True, default='place', max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='country',
            field=models.CharField(blank=True, default='place', max_length=10),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='zipcode',
            field=models.CharField(blank=True, default='place', max_length=10),
        ),
    ]
