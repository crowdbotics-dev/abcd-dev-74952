# Generated by Django 2.2.28 on 2023-04-07 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_testdatamodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='testdatamodel',
            name='testnew',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
