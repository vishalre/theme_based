# Generated by Django 2.0.2 on 2019-03-28 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0004_detailsmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
            ],
        ),
    ]
