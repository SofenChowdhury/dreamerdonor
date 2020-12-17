# Generated by Django 3.0.3 on 2020-10-13 15:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='assets/uploads/user')),
                ('role', models.CharField(blank=True, choices=[('Admin', 'Admin'), ('Dreamer', 'Dreamer'), ('Donor', 'Donor')], default='Dreamer', max_length=20)),
                ('user_code', models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True)),
                ('join_date', models.DateField(blank=True, default=datetime.date.today)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]