# Generated by Django 2.2.5 on 2019-09-25 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GridLocked', '0013_auto_20190925_1451'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attribute',
            old_name='nemesis_attribute',
            new_name='bonus_vs',
        ),
    ]
