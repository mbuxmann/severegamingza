# Generated by Django 2.1.5 on 2019-01-30 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0010_auto_20190130_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='hook',
            field=models.TextField(max_length=300),
        ),
    ]