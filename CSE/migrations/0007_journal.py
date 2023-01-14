# Generated by Django 4.1.4 on 2023-01-14 15:48

import CSE.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSE', '0006_remove_conference_faculty_name_delete_faculty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('journal_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('journal_name', models.CharField(max_length=255)),
                ('journal_article', models.FileField(upload_to='journals/', validators=[CSE.models.validate_pdf])),
                ('journal_doi', models.IntegerField()),
                ('ugc_listed', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=10)),
            ],
        ),
    ]