# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('substance', models.CharField(max_length=30)),
                ('lastMeeting', models.DateField()),
                ('checked_in', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=70)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='login',
            name='user_id',
            field=models.ForeignKey(to='patient.Patient'),
        ),
    ]
