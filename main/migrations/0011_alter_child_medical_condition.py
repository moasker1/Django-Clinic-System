# Generated by Django 4.1.7 on 2023-05-21 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_child_medical_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='medical_condition',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
