# Generated by Django 5.0.6 on 2024-05-27 10:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('role', models.CharField(max_length=20, verbose_name='Role')),
                ('last_updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_last_updated_by', to=settings.AUTH_USER_MODEL)),
                ('registered_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_registered_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('airtel_number', models.CharField(max_length=15, verbose_name='Airtel No')),
                ('mtn_number', models.CharField(max_length=15, verbose_name='MTN No')),
                ('last_updated_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_last_updated_by', to=settings.AUTH_USER_MODEL)),
                ('registered_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='%(class)s_registered_by', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('role', models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='facilitators.role')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
