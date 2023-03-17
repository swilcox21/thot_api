# Generated by Django 4.1.4 on 2023-03-17 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reminder',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='reminder',
            name='dashboard',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='reminder',
            name='order',
            field=models.IntegerField(default=1),
        ),
    ]
