# Generated by Django 3.0.4 on 2020-03-20 20:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_agreec'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='agreec',
            new_name='agree',
        ),
    ]
