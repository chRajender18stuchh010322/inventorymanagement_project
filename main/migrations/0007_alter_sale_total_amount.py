# Generated by Django 3.2.7 on 2021-09-20 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210920_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='total_amount',
            field=models.FloatField(editable=False),
        ),
    ]
