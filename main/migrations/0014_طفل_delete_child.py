# Generated by Django 4.1.7 on 2023-05-22 14:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_rename_child_id_child_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='طفل',
            fields=[
                ('الاسم', models.CharField(max_length=100)),
                ('تاريح_الحجز', models.DateField(default=datetime.date.today)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('رقم_التليفون', models.CharField(max_length=20)),
                ('الحالة', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Child',
        ),
    ]
