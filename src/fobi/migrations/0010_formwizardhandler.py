# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-12 21:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models

from django_nine import versions

class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fobi', '0009_formwizardentry_wizard_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormWizardHandler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plugin_uid', models.CharField(editable=False, max_length=255, unique=True, verbose_name='Plugin UID')),
                ('groups', models.ManyToManyField(blank=True, to='auth.Group', verbose_name='Group')),
                ('users', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Form wizard handler plugin',
                'verbose_name_plural': 'Form wizard handler plugins',
            },
        ),
    ]
