# Generated by Django 5.0.6 on 2024-05-27 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_temperaturadata_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperaturadata',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
