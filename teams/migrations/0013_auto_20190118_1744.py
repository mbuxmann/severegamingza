# Generated by Django 2.1.5 on 2019-01-18 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0012_auto_20190118_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='counterstrikeplayer',
            name='Username',
            field=models.CharField(default='In Game Name', max_length=100),
        ),
        migrations.AddField(
            model_name='dota2player',
            name='Username',
            field=models.CharField(default='In Game Name', max_length=100),
        ),
    ]