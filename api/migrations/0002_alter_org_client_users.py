# Generated by Django 4.1.4 on 2023-05-09 09:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='org',
            name='client_users',
            field=models.ManyToManyField(blank=True, related_name='clients', to=settings.AUTH_USER_MODEL),
        ),
    ]
