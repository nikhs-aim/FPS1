# Generated by Django 4.1.4 on 2023-01-14 09:15

import CSE.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSE', '0003_alter_conference_ugc_listed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conference',
            name='conference_article',
            field=models.FileField(upload_to='conferences/', validators=[CSE.models.validate_pdf]),
        ),
    ]
