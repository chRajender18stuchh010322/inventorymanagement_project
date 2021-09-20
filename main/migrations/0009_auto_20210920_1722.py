# Generated by Django 3.2.7 on 2021-09-20 11:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20210920_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.customer'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='vender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.vendor'),
        ),
    ]