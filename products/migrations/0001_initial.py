# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_name', models.CharField(max_length=40000)),
                ('serial_number', models.CharField(max_length=40000)),
                ('warranty_info', models.CharField(max_length=40000)),
                ('img', models.ImageField(upload_to=b'product_photos')),
                ('pdf', models.ImageField(upload_to=b'product_pdfs')),
            ],
        ),
    ]
