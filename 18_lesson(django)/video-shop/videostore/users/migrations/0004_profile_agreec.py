# Generated by Django 3.0.4 on 2020-03-20 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200320_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='agreec',
            field=models.BooleanField(default=True),
        ),
    ]
