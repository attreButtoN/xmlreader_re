# Generated by Django 3.2.6 on 2021-10-29 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xmlinport', '0051_alter_dealinvalid_declaration_notice_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lottable',
            old_name='auctiot_lot',
            new_name='auction_lot',
        ),
    ]
