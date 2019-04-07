# Generated by Django 2.0.2 on 2019-03-29 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginapp', '0005_login_details'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login_details',
        ),
        migrations.AddField(
            model_name='detailsmodel',
            name='speed',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='detailsmodel',
            name='carImg',
            field=models.ImageField(upload_to='loginapp/images/'),
        ),
    ]