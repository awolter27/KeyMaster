# Generated by Django 4.2.3 on 2023-07-11 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_rename_records_record'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='website',
            field=models.CharField(default='NA', max_length=50),
            preserve_default=False,
        ),
    ]