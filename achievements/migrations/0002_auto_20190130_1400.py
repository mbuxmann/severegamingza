# Generated by Django 2.1.5 on 2019-01-30 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('achievements', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='division',
            field=models.CharField(choices=[('Premier', 'Premier'), ('First', 'First'), ('Second', 'Second'), ('Ladder', 'Ladder')], max_length=10),
        ),
    ]
