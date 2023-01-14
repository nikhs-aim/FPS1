# Generated by Django 4.1.4 on 2023-01-14 07:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('conference_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('conference_name', models.CharField(max_length=255)),
                ('conference_article', models.ImageField(upload_to='conferences/')),
                ('conference_doi', models.IntegerField()),
                ('ugc_listed', models.CharField(choices=[('up', 'yes'), ('down', 'no')], max_length=10)),
            ],
        ),
    ]
