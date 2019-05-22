# Generated by Django 2.1.5 on 2019-01-18 07:04

from django.db import migrations, models
import precise_bbcode.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_article_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='_hook_rendered',
            field=models.TextField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='hook',
            field=precise_bbcode.fields.BBCodeTextField(default='General', no_rendered_field=True),
        ),
    ]
