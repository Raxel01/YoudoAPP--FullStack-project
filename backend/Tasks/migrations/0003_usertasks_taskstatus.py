# Generated by Django 4.2.13 on 2024-10-25 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tasks', '0002_alter_usertasks_options_usertasks_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertasks',
            name='TaskStatus',
            field=models.CharField(default='STARTED', max_length=12),
        ),
    ]
