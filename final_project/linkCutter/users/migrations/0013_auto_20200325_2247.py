# Generated by Django 3.0.4 on 2020-03-25 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_profile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='img',
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]
