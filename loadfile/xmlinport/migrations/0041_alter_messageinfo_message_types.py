# Generated by Django 3.2.6 on 2021-10-28 14:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xmlinport', '0040_alter_bankrupt_person_v2_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messageinfo',
            name='message_types',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='xmlinport.messagetypes'),
        ),
    ]