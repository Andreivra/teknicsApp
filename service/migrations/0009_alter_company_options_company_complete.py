# Generated by Django 4.2.2 on 2023-07-06 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_remove_company_agent_alter_company_agent_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['complete']},
        ),
        migrations.AddField(
            model_name='company',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
