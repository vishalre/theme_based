# Generated by Django 2.0.2 on 2019-03-29 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0006_auto_20190329_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailsmodel',
            name='speed',
            field=models.CharField(max_length=10, null=True),
        ),
    ]