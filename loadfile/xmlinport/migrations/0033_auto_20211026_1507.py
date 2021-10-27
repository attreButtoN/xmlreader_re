# Generated by Django 3.2.6 on 2021-10-26 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xmlinport', '0032_viewdraftrestructuringplan_bankruptcy_acknowledgment_and_start_of_restructuring_messageid'),
    ]

    operations = [
        migrations.AddField(
            model_name='changedeliberatebankruptcy',
            name='deliberate_bankruptcy_signs',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='changedeliberatebankruptcy',
            name='deliberate_signs_not_searched_reason',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='changedeliberatebankruptcy',
            name='fake_bankruptcy_signs',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='changedeliberatebankruptcy',
            name='fake_signs_not_searched_reason',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='changedeliberatebankruptcy',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Text'),
        ),
    ]
