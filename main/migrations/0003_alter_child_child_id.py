# Generated by Django 4.1.7 on 2023-05-20 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_child_id_alter_child_child_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='child_id',
            field=models.AutoField(default=100, primary_key=True, serialize=False),
        ),
    ]