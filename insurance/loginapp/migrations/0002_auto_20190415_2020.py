# Generated by Django 2.1.7 on 2019-04-15 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detailsmodel',
            old_name='user',
            new_name='username',
        ),
    ]