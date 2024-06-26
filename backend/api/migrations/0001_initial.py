# Generated by Django 5.0.1 on 2024-06-26 09:40

import django.db.models.deletion
import encrypted_model_fields.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_of_registration', models.DateField()),
                ('registration_number', encrypted_model_fields.fields.EncryptedCharField()),
                ('address', models.TextField()),
                ('contact_person', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('employee_id', encrypted_model_fields.fields.EncryptedCharField()),
                ('department', models.CharField(max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.company')),
            ],
        ),
        migrations.CreateModel(
            name='RoleHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=255)),
                ('date_started', models.DateField()),
                ('date_left', models.DateField(blank=True, null=True)),
                ('duties', models.TextField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.employee')),
            ],
        ),
    ]
