# Generated by Django 2.1.7 on 2019-03-18 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190312_0120'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='zip_code',
            field=models.CharField(default='', max_length=6),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
