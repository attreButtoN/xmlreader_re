# Generated by Django 3.2.6 on 2021-10-22 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xmlinport', '0010_auto_20211022_0937'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publisher',
            old_name='publisher',
            new_name='xsi_type',
        ),
    ]