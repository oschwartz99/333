# Generated by Django 2.1.7 on 2019-03-31 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0007_auto_20190323_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='number_going',
            field=models.IntegerField(default=0),
        ),
    ]
