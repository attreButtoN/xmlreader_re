# Generated by Django 3.2.6 on 2021-10-26 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xmlinport', '0031_alter_meetingworker_meeting_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='viewdraftrestructuringplan',
            name='bankruptcy_acknowledgment_and_start_of_restructuring_messageid',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
