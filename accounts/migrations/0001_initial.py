# Generated by Django 2.1.5 on 2019-02-25 11:27

import autithi.utils.location
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('city', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_email', message='Email must be alphanumaric or contain any of following". @"', regex='^[a-z0-9.@]*$')], verbose_name='email address')),
                ('username', models.CharField(max_length=255)),
                ('date_of_birth', models.DateField()),
                ('phone_number', models.CharField(max_length=255)),
                ('zipcode', models.CharField(default='1000', max_length=120)),
                ('profile_image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=autithi.utils.location.upload_location, width_field='width_field')),
                ('description', models.TextField(max_length=255)),
                ('profession', models.CharField(max_length=255)),
                ('id_image1', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=autithi.utils.location.upload_location, width_field='width_field')),
                ('id_imege2', models.ImageField(blank=True, height_field='height_field', null=True, upload_to=autithi.utils.location.upload_location, width_field='width_field')),
                ('id_type', models.IntegerField(blank=True, null=True)),
                ('facebook', models.CharField(max_length=255)),
                ('twitter', models.CharField(max_length=255)),
                ('linkedin', models.CharField(max_length=255)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('city', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='city.City')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField()),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
