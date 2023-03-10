# Generated by Django 4.1.4 on 2023-01-15 12:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('CSE', '0007_journal'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('dept_name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
