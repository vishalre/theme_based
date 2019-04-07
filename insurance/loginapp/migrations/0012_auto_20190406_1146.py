# Generated by Django 2.1.7 on 2019-04-06 06:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0011_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(on_delete='cascade', to=settings.AUTH_USER_MODEL),
        ),
    ]