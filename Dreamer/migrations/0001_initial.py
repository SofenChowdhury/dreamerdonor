# Generated by Django 3.0.3 on 2020-10-13 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=15, null=True)),
                ('sub_title', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('plan_doc', models.FileField(blank=True, null=True, upload_to='assets/uploads/user')),
                ('video', models.FileField(blank=True, null=True, upload_to='assets/uploads/user')),
                ('video_link', models.TextField(blank=True, null=True)),
                ('idea_code', models.CharField(blank=True, default=uuid.uuid4, max_length=100, unique=True)),
                ('posted_time', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='IdeaImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='assets/uploads/Idea')),
                ('idea_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dreamer.Idea')),
            ],
        ),
    ]
