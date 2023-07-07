# Generated by Django 4.2.2 on 2023-07-06 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0001_initial'),
        ('service', '0006_rename_agent_company_agent_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='agent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='agent.agent'),
        ),
        migrations.AlterField(
            model_name='company',
            name='agent_name',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]