# Generated by Django 2.1.7 on 2019-03-23 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0006_auto_20190323_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('Party', 'Party'), ('Concert', 'Concert')], max_length=50),
        ),
    ]
