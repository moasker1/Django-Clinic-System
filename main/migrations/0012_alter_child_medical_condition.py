# Generated by Django 4.1.7 on 2023-05-21 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_child_medical_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='medical_condition',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
