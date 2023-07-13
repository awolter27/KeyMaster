# Generated by Django 4.2.3 on 2023-07-13 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_record_website'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='record',
            options={'ordering': ['website']},
        ),
        migrations.AlterField(
            model_name='record',
            name='notes',
            field=models.TextField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='record',
            name='security_key',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='record',
            name='security_questions',
            field=models.TextField(max_length=1000),
        ),
    ]