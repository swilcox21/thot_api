# Generated by Django 4.1.4 on 2023-03-17 03:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_groop_thot'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thot',
            old_name='folder',
            new_name='groop',
        ),
    ]
