# Generated by Django 4.1.4 on 2023-03-17 03:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_alter_reminder_options_reminder_dashboard_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('order', models.IntegerField(default=1)),
                ('home', models.BooleanField(default=True)),
                ('hidden', models.BooleanField(default=False)),
                ('image', models.CharField(default='', max_length=5000)),
                ('name', models.CharField(max_length=50, unique=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groops', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Thot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('order', models.IntegerField(default=1)),
                ('text', models.CharField(max_length=5000)),
                ('dashboard', models.BooleanField(default=False)),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thots', to='api.groop')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]