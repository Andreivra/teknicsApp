# Generated by Django 4.2.2 on 2023-07-06 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_rename_agent_name_company_agent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='agent',
            new_name='agent_name',
        ),
    ]