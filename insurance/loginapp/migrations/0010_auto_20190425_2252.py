# Generated by Django 2.1.7 on 2019-04-25 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0009_detailsmodel_damagedpart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='license',
            field=models.CharField(max_length=10),
        ),
    ]
