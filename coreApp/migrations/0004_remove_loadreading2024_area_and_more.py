# Generated by Django 5.1.6 on 2025-03-04 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreApp', '0003_loadreading2024_alter_profile_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loadreading2024',
            name='area',
        ),
        migrations.RemoveField(
            model_name='loadreading2024',
            name='consremarks',
        ),
        migrations.RemoveField(
            model_name='loadreading2024',
            name='consteng',
        ),
        migrations.RemoveField(
            model_name='loadreading2024',
            name='gov',
        ),
        migrations.RemoveField(
            model_name='loadreading2024',
            name='pending_with',
        ),
        migrations.RemoveField(
            model_name='loadreading2024',
            name='recieved_by_construction',
        ),
        migrations.RemoveField(
            model_name='loadreading2024',
            name='schemes_in_process',
        ),
        migrations.AlterField(
            model_name='loadreading2024',
            name='uspdate',
            field=models.CharField(default='', max_length=255, verbose_name='USPDATE'),
            preserve_default=False,
        ),
    ]
