# Generated by Django 2.1.7 on 2019-04-20 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0006_auto_20190420_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='licenseplate',
            field=models.CharField(default='licenseplate', max_length=50),
        ),
    ]