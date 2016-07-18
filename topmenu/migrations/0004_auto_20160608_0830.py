# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-08 15:30
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion

def _create_user_if_no_user_exists(apps, schema_editor):
    User = apps.get_model('topmenu', 'User')
    User.objects.create(username='placeholder', password='placeholder', phone_num=0, user_state=1, user_sms_quant=0)

class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('topmenu', '0003_auto_20160528_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='SMS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_uuid', models.CharField(max_length=40)),
                ('source', models.PositiveIntegerField(max_length=11)),
                ('destination', models.PositiveIntegerField(max_length=11)),
                ('message_content', models.CharField(max_length=140)),
                ('message_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('phone_num', models.PositiveIntegerField(max_length=10)),
                ('user_jointime', models.DateTimeField(auto_now_add=True)),
                ('user_state', models.PositiveIntegerField(max_length=2)),
                ('user_sms_quant', models.PositiveIntegerField(max_length=4)),
                ('user_language', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='listing',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name='sms',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topmenu.User'),
        ),

        migrations.RunPython(
            code=_create_user_if_no_user_exists
        ),

        migrations.AddField(
            model_name='listing',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='topmenu.User'),
            preserve_default=False,
        ),
    ]
