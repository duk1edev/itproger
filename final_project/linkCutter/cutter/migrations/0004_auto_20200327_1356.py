# Generated by Django 3.0.4 on 2020-03-27 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cutter', '0003_auto_20200326_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='url_name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Short url name'),
        ),
    ]
