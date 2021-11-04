# Generated by Django 3.2.6 on 2021-10-28 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xmlinport', '0037_auto_20211028_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankrupt',
            name='bankrupt',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Bankrupt'),
        ),
        migrations.AlterField(
            model_name='bankrupt_person_v2',
            name='address',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='bankrupt_person_v2',
            name='birth_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='BirthDate'),
        ),
        migrations.AlterField(
            model_name='bankrupt_person_v2',
            name='birth_place',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='BirthPlace'),
        ),
        migrations.AlterField(
            model_name='bankrupt_person_v2',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='xmlinport.category'),
        ),
        migrations.AlterField(
            model_name='bankrupt_person_v2',
            name='fio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='xmlinport.fio'),
        ),
        migrations.AlterField(
            model_name='bankrupt_person_v2',
            name='fio_history',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='xmlinport.fiohistory', verbose_name='FioHistory'),
        ),
        migrations.AlterField(
            model_name='bankrupt_person_v2',
            name='inn',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='INN'),
        ),
        migrations.AlterField(
            model_name='bankrupt_person_v2',
            name='snils',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='SNILS'),
        ),
        migrations.AlterField(
            model_name='fileinfo',
            name='hash',
            field=models.TextField(null=True, verbose_name='Hash'),
        ),
        migrations.AlterField(
            model_name='fileinfo',
            name='name',
            field=models.TextField(null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='fileinfolist',
            name='file_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='xmlinport.fileinfo'),
        ),
        migrations.AlterField(
            model_name='messageurl',
            name='download_size',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='messageurl',
            name='url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='messageurl',
            name='url_name',
            field=models.TextField(blank=True, null=True),
        ),
    ]