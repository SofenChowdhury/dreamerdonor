# Generated by Django 3.0.5 on 2020-10-18 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='Dreamer & Donor', max_length=200)),
                ('logo', models.ImageField(blank=True, upload_to='assets/uploads/setup')),
                ('fb', models.CharField(blank=True, max_length=200)),
                ('youtube', models.CharField(blank=True, max_length=200)),
                ('insta', models.CharField(blank=True, max_length=200)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('address', models.CharField(blank=True, max_length=300)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('country', models.CharField(blank=True, max_length=100)),
                ('start_time', models.TimeField(blank=True, default='10:00:00')),
                ('end_time', models.TimeField(blank=True, default='18:00:00')),
            ],
            options={
                'verbose_name_plural': 'Contact Us',
            },
        ),
        migrations.CreateModel(
            name='TermsCondition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Terms & Conditions',
            },
        ),
    ]
