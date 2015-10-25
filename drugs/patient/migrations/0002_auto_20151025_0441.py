# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='user_id',
        ),
        migrations.AddField(
            model_name='login',
            name='password',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AddField(
            model_name='login',
            name='username',
            field=models.ForeignKey(to='patient.Patient', default=b'', to_field=b'email'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(unique=True, max_length=70),
        ),
    ]
