# Generated by Django 3.2.6 on 2021-10-29 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xmlinport', '0046_rename_selection_purchaser_assest_messagetypes_selection_purchaser_assets'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messagetypes',
            old_name='bank_open_accout_debtor',
            new_name='bank_open_account_debtor',
        ),
        migrations.RenameField(
            model_name='messagetypes',
            old_name='part_build_monetaty_claim',
            new_name='part_build_monetary_claim',
        ),
    ]