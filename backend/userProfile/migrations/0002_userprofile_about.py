# Generated by Django 3.1.5 on 2021-01-06 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='about',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]