# Generated by Django 4.1.4 on 2023-01-15 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CSE', '0010_conference_fac_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='fac_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
