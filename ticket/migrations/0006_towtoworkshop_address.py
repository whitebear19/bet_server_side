# Generated by Django 3.1.2 on 2020-12-19 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0005_auto_20201217_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='towtoworkshop',
            name='address',
            field=models.CharField(default='', max_length=255, null=True),
        ),
    ]
